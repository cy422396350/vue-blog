<template>
  <div class="vuelog">
      <transition appear name="fade" mode="out-in">
          <vue-header v-if="guide"></vue-header>
      </transition>
      <router-view @showbox="toshow"></router-view>
  </div>
</template>

<script>
  import vueHeader from './components/Header.vue'
  export default {
    components:{
      vueHeader,
    },
    name:'index',
    data(){
      return {
        guide:0
      }
    },
    compute:{
    },
    watch: {

    },
    methods:{
      resetScroll(){
        window.scroll(0,0)
      },
      toshow(guide) {
        this.guide = guide;
      }
    }
  }
</script>

<style lang="scss">
  @import './assets/style/global.scss';
  @import './assets/style/animate.css';
</style>
