/**
 * Created by MBENBEN on 2017/7/16.
 */
export default {
  install(Vue,options){
    Vue.prototype.buildUrl = function(url){
      return url+"?showapi_appid="+this.$store.state.config.appid+"&showapi_timestamp="
        +new Date().Format("yyyyMMddhhmmss")+"&showapi_sign="+this.$store.state.config.secret
    }
  }
}
