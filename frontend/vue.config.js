var BundleTracker = require('webpack-bundle-tracker');

module.exports = {
    outputDir: '../modoboa_imap_migration/static/',
    assetsDir: 'modoboa_imap_migration',
    baseUrl: process.env.NODE_ENV === 'production'
           ? '/sitestatic/'
           : 'http://localhost:8080/',
    devServer: {
        publicPath: 'http://localhost:8080/',
        headers: {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, PATCH, OPTIONS',
            'Access-Control-Allow-Headers':
            'X-Requested-With, content-type, Authorization',
            'Access-Control-Allow-Credentials': 'true'
        }
    },
    configureWebpack: config => {
        config.plugins.push(new BundleTracker({
            path: '../modoboa_imap_migration/static/'
        }));
    }
}
