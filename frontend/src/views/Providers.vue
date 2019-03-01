<template>
<div>
  <div class="row">
    <div class="col-sm-5">
      <search-form @search="(query) => getProviders(query)"></search-form>
    </div>
    <div class="col-sm-7">
      <button type="button" class="btn btn-primary" @click="showProviderForm = true">
        <span class="fa fa-plus"></span>&nbsp;<translate>Add</translate>
      </button>
    </div>
  </div>
  <table v-if="providers" class="table">
    <thead>
      <tr>
        <th><translate>Name</translate></th>
        <th><translate>Address</translate></th>
        <th><translate>Port</translate></th>
        <th></th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="provider in providers" :key="`provider-${provider.id}`">
        <td>{{ provider.name }}</td>
        <td>{{ provider.address }}</td>
        <td>{{ provider.port }}</td>
        <td class="text-right">
          <button type="button" @click="editProvider(provider)" class="btn btn-primary btn-xs"><span class="fa fa-edit"></span></button>
          <button type="button" @click="deleteProvider(provider)" class="btn btn-danger btn-xs"><span class="fa fa-trash"></span></button>
        </td>
      </tr>
    </tbody>
  </table>
  <provider-form v-if="showProviderForm"
                 :initialProvider="editedProvider"
                 @close="closeProviderForm">
  </provider-form>
</div>
</template>

<script>
import { mapGetters } from 'vuex'
import ProviderForm from '@/components/ProviderForm.vue'
import SearchForm from '@/components/SearchForm.vue'

export default {
    components: {
        'provider-form': ProviderForm,
        'search-form': SearchForm
    },
    computed: mapGetters('providers', ['providers']),
    data () {
        return {
            editedProvider: { domains: [{}] },
            showProviderForm: false
        }
    },
    methods: {
        resetProvider () {
            this.editedProvider = { domains: [{}] }
        },
        closeProviderForm () {
            this.showProviderForm = false
            this.resetProvider()
        },
        editProvider (provider) {
            this.editedProvider = provider
            this.showProviderForm = true
        },
        deleteProvider (provider) {
            this.$store.dispatch('providers/deleteEmailProvider', provider)
        },
        getProviders (query) {
            this.$store.dispatch('providers/listEmailProviders', query)
        }
    },
    mounted () {
        this.$store.dispatch('providers/listEmailProviders')
        this.$store.dispatch('providers/listDomains')
    }
}
</script>

<style lang="scss">
.btn {
    margin: 0 2px;
}
</style>
