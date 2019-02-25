import Vue from 'vue'
import Vuex from 'vuex'

import providers from './providers'

Vue.use(Vuex)

export default new Vuex.Store({
    modules: {
        providers
    }
})
