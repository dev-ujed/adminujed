import { defineConfig } from 'vite'
import vue from "@vitejs/plugin-vue";
import { djangoVitePlugin } from 'django-vite-plugin'

export default defineConfig(({ command }) => ({
    plugins: [
        djangoVitePlugin([
            'resources/js/main.js',
            'resources/css/main.scss',
        ]),
        vue({
            template: {
                transformAssetUrls: {
                    // The Vue plugin will re-write asset URLs, when referenced
                    // in Single File Components, to point to the Laravel web
                    // server. Setting this to `null` allows the Laravel plugin
                    // to instead re-write asset URLs to point to the Vite
                    // server instead.
                    base: null,

                    // The Vue plugin will parse absolute URLs and treat them
                    // as absolute paths to files on disk. Setting this to
                    // `false` will leave absolute URLs un-touched so they can
                    // reference assets in the public directory as expected.
                    includeAbsolute: false,
                },
            },
        }),
    ],
    publicDir: command === 'serve' ? 'public' : false,
    css: {
        preprocessorOptions: {
            scss: {
                quietDeps: true,
                silenceDeprecations: ['import', 'global-builtin', 'mixed-decls', 'slash-div'],
            }
        }
    },
    resolve: {
        alias: {
            'vue': 'vue/dist/vue.esm-bundler.js',
			// 'vue': '@vue/runtime-dom',
            '~': '/node_modules/',
        },
    },
    build: {
        rollupOptions: {
            output: {
                manualChunks(id) {
                    if (id.includes('node_modules')) return 'vendor';
                },
            }
        }
    }
}));