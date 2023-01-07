<script setup lang="ts">
import QRCodeScanner from '@/components/QRCodeScanner.vue';
</script>

<template>
  <main>
    <h2>Nie możesz znaleźć sali?</h2>
    <p>Zeskanuj nabliższy kod QR</p>

    <QRCodeScanner></QRCodeScanner>

    <RouterLink :to="{ name: 'select-start', params: {} }">Lub zaznacz gdzie jesteś na liście</RouterLink>
  </main>
</template>
