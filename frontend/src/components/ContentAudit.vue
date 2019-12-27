<template>
  <div>
       {{csrf_token}}
    <span>这是学员信息页面</span>
    <button @click="getStudents">点击获取学生信息</button>
    <button @click="changeStudents">点击修改学生信息</button>
    <div v-if="isShow">
      <table border="1">
      <thead>
        <tr>
          <th>学生ID</th>
          <th>学生姓名</th>
          <th>学生电话</th>
          <th>学生地址</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(student, index) in students" :key="index">
          <td>{{ student.student_id }}</td>
          <td><input v-model="student.student_name"/></td>
          <td><input v-model="student.student_phone"/></td>
          <td><input v-model="student.student_address"/></td>
        </tr>
      </tbody>
    </table>
    </div>
  </div>
</template>

<script>
  export default {
    name: "Students",
    data() {
      return {
        isShow: false,
        students: []
      }
    },
    methods: {
      getStudents: function () {
        let ts = this;
        this.$axios.get('/api/student/1/')
          .then(function (response) {
            console.log(response);
            ts.isShow = true;
            ts.students = response.data;
          })
          .catch(function (error) {
            console.log(error);
          })
      },
      getCookie(name) {
                var value = '; ' + document.cookie;
                var parts = value.split('; ' + name + '=');
                if (parts.length === 2) return parts.pop().split(';').shift()
            },
      changeStudents: function () {
        let ts = this;
        let result = {
          student_name: 1,
          student_id: 100001,
          student_phone: 1347658765,
          student_address: "北京市石景山区智障六中"
        }

        this.$axios.post('/api/student/2/', this.$qs.stringify({
          student_name: 1,
          student_id: 100001,
          student_phone: 1347658765,
          student_address: "北京市石景山区智障六中"
        }),{headers: {'X-CSRFToken': this.getCookie('csrftoken')}})
          .then(function (response) {
            console.log(response);
          })
          .catch(function (error) {
            console.log(error);
          })
      }
    }
  }
</script>

<style scoped>

</style>
