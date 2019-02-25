import Vue from 'vue'
import { DomainService, EmailProviderService } from '@/api'
import { ADD_PROVIDER, SET_PROVIDERS, SET_PROVIDER, DELETE_PROVIDER, SET_DOMAINS } from './types'

const state = {
    domains: [],
    providers: []
}

const getters = {
    domains: state => state.domains,
    providers: state => state.providers
}

const actions = {
    listEmailProviders ({ commit }, filter) {
        var query = {}
        if (filter !== undefined) {
            query = { params: { search: filter } }
        }
        return new EmailProviderService().list(query).then(response => {
            commit(SET_PROVIDERS, response.data)
        })
    },
    createEmailProvider ({ commit }, data) {
        return new EmailProviderService().create(data).then(response => {
            commit(ADD_PROVIDER, response.data)
        })
    },
    updateEmailProvider ({ commit }, data) {
        return new EmailProviderService().update(data.id, data).then(response => {
            commit(SET_PROVIDER, response.data)
        })
    },
    deleteEmailProvider ({ commit }, data) {
        return new EmailProviderService().delete(data.id).then(response => {
            commit(DELETE_PROVIDER, data)
        })
    },
    listDomains ({ commit }) {
        return new DomainService().list().then(response => {
            commit(SET_DOMAINS, response.data)
        })
    }
}

const mutations = {
    [SET_PROVIDERS] (state, data) {
        state.providers = data
    },
    [ADD_PROVIDER] (state, data) {
        state.providers.push(data)
    },
    [SET_PROVIDER] (state, data) {
        state.providers.filter(function (item, pos) {
            if (item.id === data.id) {
                Vue.set(state.providers, pos, data)
            }
        })
    },
    [DELETE_PROVIDER] (state, data) {
        state.providers = state.providers.filter(item => {
            return item.id !== data.id
        })
    },
    [SET_DOMAINS] (state, data) {
        state.domains = data
    }
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
}
