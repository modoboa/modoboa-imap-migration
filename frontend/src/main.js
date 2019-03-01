import Vue from 'vue'

import GetTextPlugin from 'vue-gettext'
import VuejsDialog from 'vuejs-dialog'
import 'vuejs-dialog/dist/vuejs-dialog.min.css'
import vSelect from 'vue-select'

import App from './App.vue'
import router from './router'
import store from './store'
import translations from './translations.json'

Vue.config.productionTip = false

Vue.use(GetTextPlugin, {
    availableLanguages: {
        en: 'English',
        fr: 'Français'
    },
    translations: translations
})
Vue.component('v-select', vSelect)
Vue.filter('translate', value => {
    return !value ? '' : Vue.prototype.$gettext(value.toString())
})
Vue.use(VuejsDialog)

/* global userLang */
Vue.config.language = userLang

new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app')
