/**
 * Created by MBENBEN on 2017/7/16.
 */
import Vue from 'vue'
import Vuex from 'vuex'
import config from './config.js'

Vue.use(Vuex)

const state = {
  config,
}

/*const state = {
  title: database.config.brand,
  lang: database.config.defaultLang,
  menu: false,
  system: { brand, project, version },
  database,
  languages
}*/
const store = new Vuex.Store({
  state
})

export default store
