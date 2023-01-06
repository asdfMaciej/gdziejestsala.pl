<script setup lang="ts">
</script>

<template>
  <main>
    <h2>Nie możesz znaleźć sali?</h2>
    <p>Zeskanuj nabliższy kod QR</p>

    <RouterLink :to="{ name: 'select-start', params: {} }">Lub zaznacz gdzie jesteś na liście</RouterLink>
  </main>
</template>
