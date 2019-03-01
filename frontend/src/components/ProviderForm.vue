<template>
<modal :show="true">
  <div slot="header">
    <h3 class="modal-title">{{ title }}</h3>
  </div>
  <div slot="body">
    <form class="form-horizontal" method="post" @submit.prevent="save">
      <m-textfield :label="'Name' | translate"
                   v-model="provider.name"
                   :error="errors.name !== undefined"
                   :errorMessages="errors.name">
      </m-textfield>
      <m-textfield :label="'Address' | translate"
                   v-model="provider.address"
                   :error="errors.address !== undefined"
                   :errorMessages="errors.address">
      </m-textfield>
      <m-textfield :label="'Port' | translate"
                   v-model="provider.port"
                   :error="errors.port !== undefined"
                   :errorMessages="errors.port">
      </m-textfield>
      <m-checkbox :label="'Secured connection' | translate"
                  v-model="provider.secured">
      </m-checkbox>
      <hr>
      <p class="header">Associated domains</p>
      <div class="row" v-for="(domain, index) in provider.domains"
           :key="`domain-${index}`">
        <div class="col-sm-5">
          <m-textfield :placeholder="'Domain name' | translate"
                       labelWidth=""
                       inputWidth="col-sm-12"
                       v-model="domain.name">
          </m-textfield>
        </div>
        <div class="col-sm-5">
          <v-select :placeholder="'Rename to' | translate"
                    :options="domains"
                    label="name"
                    index="pk"
                    v-model="domain.new_domain">
          </v-select>
        </div>
        <div class="col-sm-2">
          <a href="#" class="btn btn-default btn-xs" @click="addDomain"><span class="fa fa-plus"></span></a>
          <a v-if="index !== 0" class="btn btn-default btn-xs" @click="removeDomain(index)" href="#">
            <span class="fa fa-trash"></span>
          </a>
        </div>
      </div>
      <hr>
      <div class="pull-right">
        <button type="button" class="btn btn-default" @click="close"><translate>Close</translate></button>
        <input type="submit" class="btn btn-primary" value="Save">
      </div>
      <div class="clearfix"></div>
    </form>
  </div>
</modal>
</template>

<script>
import { mapGetters } from 'vuex'
import Modal from './Modal.vue'
import Checkbox from './Checkbox.vue'
import TextField from './TextField.vue'

export default {
    components: {
        modal: Modal,
        'm-checkbox': Checkbox,
        'm-textfield': TextField
    },
    computed: {
        ...mapGetters('providers', ['domains']),
        title () {
            return (this.provider.id === undefined)
                ? this.$gettext('New provider')
                : this.$gettext('Edit provider')
        }
    },
    data () {
        return {
            errors: {},
            provider: this.loadProvider(this.initialProvider)
        }
    },
    methods: {
        addDomain () {
            this.provider.domains.push({})
        },
        removeDomain (index) {
            this.provider.domains.splice(index, 1)
        },
        close () {
            this.$emit('close')
            this.errors = {}
            this.provider = {}
        },
        loadProvider (value) {
            if (value) {
                let result = JSON.parse(JSON.stringify(value))
                if (!result.domains.length) {
                    result.domains = [{}]
                }
                return result
            }
            return { domains: [{}] }
        },
        save () {
            var action = (this.provider.id !== undefined)
                ? 'providers/updateEmailProvider'
                : 'providers/createEmailProvider'
            this.$store.dispatch(action, this.provider).then(response => {
                this.close()
            }).catch(error => {
                this.errors = error.response.data
            })
        }
    },
    props: {
        initialProvider: Object
    },
    watch: {
        initialProvider (value) {
            this.loadProvider(value)
        }
    }
}
</script>

<style scoped>
.header {
    text-align: center;
    font-size: 1em;
    font-weight: 600;
    color: #bbb;
}
</style>
