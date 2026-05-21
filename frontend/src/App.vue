<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const articles = ref([])
const loading = ref(true)

const fetchNews = async () => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/news')
    articles.value = response.data
  } catch (error) {
    console.error(error)
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  fetchNews()
})
</script>

<template>
  <div class="app">
    <div class="background-glow"></div>

    <header class="hero">
      <h1>Crypto News Aggregator</h1>
      <p>Stay updated with the latest news in the cryptocurrency world</p>
    </header>

    <div class="content">
      <div v-if="loading" class="loading-card">
        Loading latest news...
      </div>

      <a
        v-for="article in articles"
        :key="article.link"
        :href="article.link"
        target="_blank"
        class="news-card"
      >
        <div class="news-content">
          <h2>{{ article.title }}</h2>
          <p>Open article →</p>
        </div>
      </a>
    </div>
  </div>
</template>
<style>

.content {
  position: relative;
  z-index: 1;
  max-width: 900px;
  margin: auto;
  display: grid;
  gap: 1.25rem;
}

.news-card {
  text-decoration: none;
  color: white;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.08);
  backdrop-filter: blur(12px);
  border-radius: 20px;
  padding: 1.5rem;
  transition: all 0.25s ease;
}

.news-card:hover {
  transform: translateY(-4px);
  border-color: rgba(120, 150, 255, 0.5);
  background: rgba(255, 255, 255, 0.08);
}

.news-content h2 {
  margin: 0 0 0.75rem;
  font-size: 1.2rem;
  line-height: 1.5;
}

.news-content p {
  margin: 0;
  color: #7ea1ff;
  font-size: 0.95rem;
}

.loading-card {
  background: rgba(255, 255, 255, 0.05);
  border-radius: 20px;
  padding: 2rem;
  text-align: center;
  color: #b7c0d8;
}

@media (max-width: 768px) {
  .hero h1 {
    font-size: 2.2rem;
  }

  .news-content h2 {
    font-size: 1rem;
  }
}
</style>