import Vue from 'vue'

import GetTextPlugin from 'vue-gettext'

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

Vue.filter('translate', value => {
    return !value ? '' : Vue.prototype.$gettext(value.toString())
})

/* global userLang */
Vue.config.language = userLang

new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app')
