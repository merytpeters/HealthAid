import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import svgr from "vite-plugin-svgr";

// https://vite.dev/config/
export default defineConfig({
  plugins: [svgr(), react()],
  server: {
    port: 3000,
    proxy: {
      '/api': {
        target : 'http://localhost:5000',
        changeOrigin: true,
        rewrite: ( path) => path.replace(/^\/api/, '')
      }
    }
  }
})
