<template>
  <div class="right">
    <div class="right-content category">
      <ul>
        <li v-for="item in articles">
          <div class="article-meta">
            <time datetime="2016-04-02T06:11:20.000Z">2016-04-02</time>
          </div>
          <article>
            <header>
              <router-link :to="'/article/'+item.ID" v-text="item.title"></router-link>
              <time></time>
            </header>
            <p>
              Gulp前端自动化：Gulp的高度集成化开发环境，释放了前端开发中大量时间，如css压缩、js压缩、错误检查、合并js、压缩图片、压缩html、模块构造等，只要你能想到的基本都可以通过Gulp插件去实现。
            </p>
            <footer>
              <ul>
                <li>
                  <router-link :to="'/article/'+item.ID">xxxx</router-link>
                </li>
                <li>
                  <router-link :to="'/article/'+item.ID">xxxx</router-link>
                </li>
              </ul>
            </footer>
          </article>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
    components:{
    },
    name:'index',
    data(){
        return {
            articles:null
        }
    },
    compute:{
    },
    watch: {
    },
    methods:{
        resetScroll(){
            window.scroll(0,0)
        }
    },created(){
        let url = this.$store.state.apiUrl+"index"
        this.$http.get(url).then(response => {
            // get body data
            let data = JSON.parse(response.bodyText);
            this.articles = data
        }, response => {
            // error callback
        });
    }
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
