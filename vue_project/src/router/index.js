import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Course from '@/components/Course'
Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      redirect:'/home'
    },
    {
      path: '/home',
      name: 'Home',
      component: Home
    },
    {
      path:'/course',
      name:'Course',
      component:Course

    }
  ]
})
