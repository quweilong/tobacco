<template>

	<div v-loading="isLoading" class="comp-tree">
    <div style="height: 100px">
      <div style="float: left; ">
        <span style="font-size: 18px;line-height:30px; height:30px;">用户名:</span>
      </div>
      <div style="float: left;margin-left: 150px">
        <el-input
        placeholder=""
        v-model="input"
        :disabled="true">
      </el-input>
      </div>
    </div>
    <div>
      <el-button class="comp-tr-top"
			type="primary"
			size="small"
			@click="handleAddTop">添加顶级节点</el-button>
		<!-- tree -->
		<el-tree ref="SlotTree"
			:data="setTree"
			:props="defaultProps"
             @check-change="handleCheckChange">

			:expand-on-click-node="false"
			highlight-current
			:node-key="NODE_KEY">
				<div class="comp-tr-node" slot-scope="{ node, data }">
					<!-- 编辑状态 -->
					<template v-if="node.isEdit">
						<el-input v-model="data.name"
							autofocus
							size="mini"
							:ref="'slotTreeInput'+data[NODE_KEY]"
							@blur.stop="handleInput(node, data)"
							@keyup.enter.native="handleInput(node, data)"></el-input>
					</template>

					<!-- 非编辑状态 -->
					<template v-else>
						<!-- 名称： 新增节点增加class（is-new） -->
						<span :class="[data[NODE_KEY] < NODE_ID_START ? 'is-new' : '', 'comp-tr-node--name']">
							{{ node.label }}
						</span>

						<!-- 按钮 -->
						<span class="comp-tr-node--btns">
							<!-- 新增 -->
							<el-button icon="el-icon-plus"
								size="mini"
								circle
								type="primary"
								@click="handleAdd(node, data)"></el-button>

							<!-- 编辑 -->
							<el-button icon="el-icon-edit"
								size="mini"
								circle
								type="info"
								@click="handleEdit(node, data)"></el-button>

							<!-- 删除 -->
							<el-button icon="el-icon-delete"
								size="mini"
								circle
								type="danger"
								@click="handleDelete(node, data)"></el-button>
						</span>
					</template>
				</div>
			</el-tree>
        <el-button type="primary" @click="updateTree(node, data)">保存</el-button>


    </div>


	</div>
</template>
<script>
  import api from '@/resourse/api'
  // window.onload = function () {
  //   vm.getTreeData()
  //           //方法内容
  //       }
  //       var vm = null;

export default{
	name: 'component-tree',
	data(){
		return {
			isLoading: false,// 是否加载
			setTree: [],// tree数据
			NODE_KEY: 'id',// id对应字段
			MAX_LEVEL: 3,// 设定最大层级
			NODE_ID_START: 0,// 新增节点id，逐次递减
			startId: null,
			defaultProps: {// 默认设置
				children: 'children',
				label: 'name'
			},
			initParam: {// 新增参数
				name: '新增节点',
				pid: 0,
				children: []
			},
		}
	},
	created(){

		// 初始值
    vm = this
		this.startId = this.NODE_ID_START
	},
  mounted(){
	  this.getTreeData()

  },

	methods: {
	  // 获取数据方法
	  getTreeData(){
	    console.log("jinlaila")
      var that = this
      this.$axios.get('/api/getTreeData/').then(function (response) {
        that.setTree = response.data;

      })
    },

    // 删除数据方法
    delTreeData(id){
      var that = this
      var param = {id:id}
      var that = this
	    this.$axios.delete('/api/delTreeData',{data:param}).then(function (response) {
        console.log("successssss")
        that.$message.success("删除成功")
	      that.getTreeData()    //重新加载数据

      })
    },

	  // 获取csrftoken
	  getCookie(name) {
                var value = '; ' + document.cookie;
                var parts = value.split('; ' + name + '=');
                if (parts.length === 2) return parts.pop().split(';').shift()
            },

    // 保存更新方法
	   updateTree(_node, _data){
	    var that = this
	    this.$axios.post('/api/updateTree/',this.setTree,
        {headers: {'X-CSRFToken': this.getCookie('csrftoken')}})
        .then(function (response) {
          that.$message.success("更新成功")



        })
    },
	  handleCheckChange(data, checked, indeterminate) {
        console.log("改变",data, checked, indeterminate);
      },
    // 保存
    handleSave(){hsaytiwuyerowhiefguveuytlsdhsyurufsaufyafsflasfs.

        console.log("保存",this.$refs.SlotTree.getNode());

    },
		handleDelete(_node, _data){// 删除节点
			console.log(_node, _data)
			// 判断是否存在子节点
			if(_data.children && _data.children.length !== 0){
				this.$message.error("此节点有子级，不可删除！")
				return false;
			}else{
			  // 二次确认

					this.$confirm("是否删除此节点？","提示",{
						confirmButtonText: "确认",
						cancelButtonText: "取消",
						type: "warning"
					}).then(() => {
					  console.log("1111111")
            this.delTreeData(_data.id)



					}).catch(() => {
					  this.$message.warning("已取消")
          })

				// 删除操作
				// let DeletOprate = () => {
				// 	this.$nextTick(() => {
				// 		if(this.$refs.SlotTree){
				// 			this.$refs.SlotTree.remove(_data)
				// 			this.$message.success("删除成功！")
				// 		}
				// 	})
				// }



				// 判断是否新增： 新增节点直接删除，已存在的节点要二次确认
				_data[this.NODE_KEY] < this.NODE_ID_START ? DeletOprate() : ConfirmFun()
			}
		},
		handleInput(_node, _data){// 修改节点
			console.log(_node, _data)
			// 退出编辑状态
			if(_node.isEdit){
				this.$set(_node, 'isEdit', false)
			}
		},
		handleEdit(_node, _data){// 编辑节点
			// 设置编辑状态
			if(!_node.isEdit){
				this.$set(_node, 'isEdit', true)
			}

			// 输入框聚焦
			this.$nextTick(() => {
				if(this.$refs['slotTreeInput'+_data[this.NODE_KEY]]){
					this.$refs['slotTreeInput'+_data[this.NODE_KEY]].$refs.input.focus()
				}
			})
		},
		handleAdd(_node, _data){// 新增节点
			console.log("新增",_node, _data)
			// 判断层级
			if(_node.level >= this.MAX_LEVEL){
				this.$message.warning("当前已达到"+ this.MAX_LEVEL + "级，无法新增！")
				return false;
			}

			// 参数修改
			let obj = JSON.parse(JSON.stringify(this.initParam));// copy参数
			obj.pid = _data[this.NODE_KEY];// 父id
			obj[this.NODE_KEY] = --this.startId;// 节点id：逐次递减id
			// 判断字段是否存在
			if(!_data.children){
				this.$set(_data, 'children', [])
			}
			// 新增数据
			_data.children.push(obj)

			// 展开节点
			if(!_node.expanded){
				_node.expanded = true
			}
		},
		handleAddTop(){// 添加顶部节点
			let obj = JSON.parse(JSON.stringify(this.initParam));// copy参数
			obj[this.NODE_KEY] = --this.startId;// 节点id：逐次递减id
			this.setTree.push(obj)
		}
	}
}
</script>

<style lang="scss">
	/* common */

	// 显示按钮
	.show-btns{
		opacity: 1;
	}

	/* common end */

	.comp-tree{
		width: 100%;
		max-width: 700px;
		max-height: 80vh;
		padding: 2em;
		overflow: auto;
		// 顶部按钮
		.comp-tr-top{
			width: 100px;
			margin-bottom: 2em;
      margin-right: 50em;
		}
		// 自定义节点
		.comp-tr-node{
			// label
			.comp-tr-node--name{
				display: inline-block;
				line-height: 40px;
				min-height: 40px;
				// 新增
				&.is-new{
					font-weight: bold;
				}
			}
			// button
			.comp-tr-node--btns{
				margin-left: 10px;
				opacity: 0;
				transition: opacity .1s;
				.el-button{
					transform: scale(0.8);// 缩小按钮
					& + .el-button{
						margin-left: -1px;
					}
				}
			}
		}
		// 高亮显示按钮
		.is-current{
			&>.el-tree-node__content{
				.comp-tr-node--btns{
					@extend .show-btns;
				}
			}
		}
		// 悬浮显示按钮
		.el-tree-node__content{
			&:hover{
				.comp-tr-node--btns{
					@extend .show-btns;
				}
			}
		}
	}
  .save-btns{
  }
</style>
