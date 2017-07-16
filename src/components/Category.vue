<template>
  <div>
    <ul>
      <li v-for="item in articles">
        <router-link :to="'/article/'+item._id" v-text="item.title"></router-link>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
    components:{
    },
    name:'category',
    data(){
        return {
          title:null,
          articles:null,
          current_id:null
        }
    },
    compute:{
    },
    watch: {
      current_id: function(newValue, oldValue) {
        let url = this.buildUrl(this.$store.state.config.url.articles)+"&typeId="+newValue
        this.$http.get(url).then(response => {
          // get body data
          let data = JSON.parse(response.bodyText);
          if(data.showapi_res_code===0){
            this.articles = data.showapi_res_body.pagebean.contentlist;
          }
        }, response => {
          // error callback
        });
      }
    },
    methods:{
        resetScroll(){
            window.scroll(0,0)
        }
    },
  created(){

    /**
     * 获取类别：https://route.showapi.com/90-86?
     * showapi_appid=42417
     * &
     * showapi_test_draft=false
     * &
     * showapi_timestamp=20170716212524
     * &
     * showapi_sign=664b6bfeb4edf136d46ab405319e742c
     */
    this.current_id = this.$route.params.category
    let url = this.buildUrl(this.$store.state.config.url.articles)+"&typeId="+this.current_id
    this.$http.get(url).then(response => {
      // get body data
      let data = JSON.parse(response.bodyText);
      if(data.showapi_res_code===0){
        this.articles = data.showapi_res_body.pagebean.contentlist;
      }
    }, response => {
      // error callback
    });
  },
  beforeRouteUpdate (to, from, next) {
    // 在当前路由改变，但是该组件被复用时调用
    // 举例来说，对于一个带有动态参数的路径 /foo/:id，在 /foo/1 和 /foo/2 之间跳转的时候，
    // 由于会渲染同样的 Foo 组件，因此组件实例会被复用。而这个钩子就会在这个情况下被调用。
    // 可以访问组件实例 `this`
    this.current_id = to.params.category
    next()
  },
}
</script>
