<template>
  <transition appear name="page" mode="out-in">
  <div class="right">
    <div class="right-content category">
    <ul>
      <li v-for="item in articles">
          <div class="article-meta">
              <time datetime="2016-04-02T06:11:20.000Z">2016-04-02</time>
          </div>
          <article>
              <header>
                  <router-link :to="'/article/'+item._id" v-text="item.title"></router-link>
                  <time></time>
              </header>
              <p>
                  Gulp前端自动化：Gulp的高度集成化开发环境，释放了前端开发中大量时间，如css压缩、js压缩、错误检查、合并js、压缩图片、压缩html、模块构造等，只要你能想到的基本都可以通过Gulp插件去实现。
              </p>
              <footer>
                  <ul>
                    <li>
                        <router-link :to="'/article/'+item._id">xxxx</router-link>
                    </li>
                    <li>
                        <router-link :to="'/article/'+item._id">xxxx</router-link>
                    </li>
                  </ul>
              </footer>
          </article>
      </li>
    </ul>
    </div>
  </div>
  </transition>
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
<style lang="scss">
    @import '../../static/css/font-awesome.min.css';
    $text-font-size:16px;
    .category ul {
        padding: 0;
        li {
            margin: 30px;
            position: relative;
            .article-meta {
                position: absolute;
                top: 23px;
                right: 0;
                width: 150px;
                font-size: $text-font-size;
            }
            .article-meta time:before {
                color: #999;
                content: "\f073";
                font: 17px FontAwesome;
                margin-right: 10px;
            }
            article {
                margin-bottom: 20px;
                border: 1px solid #2f2f2f;
                box-shadow: 4px 4px 18px rgba(0, 0, 0, 0.4);
                border-radius: 5px;
                header {
                    padding: 15px 0px 15px 25px;
                    a{
                        font-size: 22px;
                    }
                    a:hover{
                        color:#f3f3f3;
                        transition:all 0.6s;
                    }
                }
                p{
                    padding: 0 15px 10px 25px;
                    font-size: $text-font-size;
                    margin: 0;
                }
                footer ul {
                    padding: 0 15px 15px 25px;;
                    li{
                        &:before{
                            line-height: 18px;
                            float: left;
                            color: #999;
                            content: "\f02d";
                            font: 16px FontAwesome;
                            margin-right: 12px;
                        }
                        margin: 10px 10px 0 0;
                        display: inline-block;
                        position: relative;
                        a{
                            position: relative;
                            font-size:16px;
                            line-height: 18px;
                            display: inline-block;
                            background: #f0ad4e;
                            border-radius: 0 5px 5px 0;
                            padding: 0 5px 0 10px;
                            color: #f3f3f3;
                            height: 18px;
                            &:before{
                                content: " ";
                                width: 0px;
                                height: 0px;
                                position: absolute;
                                top: 0;
                                left: -18px;
                                border: 9px solid transparent;
                                border-right-color: #f0ad4e;
                            }
                            &:after{
                                content:" ";
                                border:1px solid #2f2f2f;
                                width: 4px;
                                height:4px;
                                display: block;
                                position: absolute;
                                left: 2px;
                                background: #fff;
                                top: 7px;
                                border-radius: 50%;
                            }
                        }
                    }
                }
            }
        }
    }
</style>