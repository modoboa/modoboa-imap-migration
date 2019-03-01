<template>
<div>
  <div class="row">
    <div class="col-sm-5">
      <search-form @search="(query) => getMigrations(query)"></search-form>
    </div>
  </div>
  <table v-if="migrations" class="table">
    <thead>
      <tr>
        <th><translate>Provider</translate></th>
        <th><translate>Old account</translate></th>
        <th><translate>New account</translate></th>
        <th></th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="migration in migrations" :key="`migration-${migration.id}`">
        <td>{{ migration.provider.name }}</td>
        <td>{{ migration.username }}</td>
        <td>{{ migration.mailbox.full_address }}</td>
        <td class="text-right">
          <button type="button"
                  @click="deleteMigration(migration)"
                  class="btn btn-danger btn-xs"><span class="fa fa-trash"></span>
          </button>
        </td>
      </tr>
    </tbody>
  </table>
</div>
</template>

<script>
import SearchForm from '@/components/SearchForm.vue'
import { MigrationService } from '@/api'

export default {
    components: {
        'search-form': SearchForm
    },
    data () {
        return {
            migrations: []
        }
    },
    methods: {
        deleteMigration (migration) {
            this.$dialog.confirm(
                this.$gettext('Remove this migration?'), {
                    cancelText: this.$gettext('Cancel'),
                    okText: this.$gettext('Proceed')
                }
            ).then(dialog => {
                new MigrationService().delete(migration.id).then(response => {
                    this.migrations = this.migrations.filter(item => {
                        return item.id !== migration.id
                    })
                })
            })
        },
        getMigrations (filter) {
            var query = {}
            if (filter !== undefined) {
                query = { params: { search: filter } }
            }
            new MigrationService().list(query).then(response => {
                this.migrations = response.data
            })
        }
    },
    mounted () {
        this.getMigrations()
    }
}
</script>
