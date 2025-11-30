import { defineConfig } from 'vite'
import { resolve } from 'path'

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        anxiety: resolve(__dirname, 'anxiety.html'),
        dyslexia: resolve(__dirname, 'dyslexia.html'),
        discalculia: resolve(__dirname, 'discalculia.html'),
        coherence: resolve(__dirname, 'coherence.html'),
      },
    },
  },
})
