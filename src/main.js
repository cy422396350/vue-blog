// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store'
import vueResource from 'vue-resource'
import util from './util'
Date.prototype.Format = function (format) {
  let o = {
    "M+": this.getMonth()+1,
    "d+": this.getDate(),
    "h+": this.getHours(),
    "m+": this.getMinutes(),
    "s+": this.getSeconds(),
  }
  if(/(y+)/.test(format)) format = format.replace(RegExp.$1,(this.getFullYear()+"").substr(4-RegExp.$1.length))
  for (let k in o){
    if(new RegExp("("+k+")").test(format)) {
      format = format.replace(RegExp.$1,(RegExp.$1.length)===1?(o[k]): ("00"+o[k]).substr(((""+o[k]).length)))
    }
  }
  return format;
}
Vue.config.productionTip = false

Vue.use(vueResource)
Vue.use(util)
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  template: '<App/>',
  components: { App }
})
