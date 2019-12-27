import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import AccessPermissions from '@/components/AccessPermissions'
import AccessStatistics from '@/components/AccessStatistics'
import ContentAudit from '@/components/ContentAudit'


Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },{
      path:'/AccessPermissions',
      name:'AccessPermissions',
      component: AccessPermissions
    },{
      path:'/AccessStatistics',
      name:'AccessStatistics',
      component: AccessStatistics
    },{
      path:'/ContentAudit',
      name:'ContentAudit',
      component: ContentAudit
    }
  ]
})
