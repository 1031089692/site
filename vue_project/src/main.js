// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
//引入axios
import Axios from 'axios'
//将axios挂载到Vue原型上
Vue.prototype.$https=Axios;
Vue.config.productionTip = false;
Vue.use(ElementUI);
Axios.defaults.baseURL = 'https://servicetest.yourgenex.com/';
Axios.defaults.headers.common['Authorization'] = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOjg5MjYsImlhdCI6MTU4MzA1MDEzMSwibmJmIjoxNTgzNjU0OTMxLCJleHAiOjE1ODU2NDIxMzF9.R1-IbP1lK0LkSJjMgHgexQ_f6d5JKCq4nyxQw-Le5V0';
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
});
