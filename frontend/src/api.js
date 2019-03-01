import axios from 'axios'

const session = axios.create({
    xsrfCookieName: 'csrftoken',
    xsrfHeaderName: 'X-CSRFToken'
})

class ApiService {
    resource = null

    getFullUrl (path) {
        return path
    }

    list (query) {
        return session.get(this.getFullUrl(this.resource), query)
    }

    get (slug, query) {
        var path = `${this.resource}${slug}/`
        return session.get(this.getFullUrl(path), query)
    }

    create (params) {
        return session.post(this.getFullUrl(this.resource), params)
    }

    update (slug, params) {
        var path = `${this.resource}${slug}/`
        return session.put(this.getFullUrl(path), params)
    }

    patch (slug, params) {
        var path = `${this.resource}${slug}/`
        return session.patch(this.getFullUrl(path), params)
    }

    delete (slug) {
        var path = `${this.resource}${slug}/`
        return session.delete(this.getFullUrl(path))
    }
}

class EmailProviderService extends ApiService {
    resource = '/api/v1/email-providers/'
}

class DomainService extends ApiService {
    resource = '/api/v1/domains/'
}

class MigrationService extends ApiService {
    resource = '/api/v1/migrations/'
}

export {
    session,
    DomainService,
    EmailProviderService,
    MigrationService
}
