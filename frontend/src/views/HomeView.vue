<script setup lang="ts">
import QRCodeScanner from '@/components/QRCodeScanner.vue';
import router from '@/router/index';

const onMatch = (pointId: string | number) => {
  console.log('onMatch called');
  router.push({
    name: 'select-destination', params: { 'start_id': pointId }
  });
};
</script>

<template>
  <main>
    <h2>Nie możesz znaleźć sali?</h2>
    <p>Zeskanuj nabliższy kod QR</p>

    <QRCodeScanner @match="onMatch"></QRCodeScanner>

    <RouterLink :to="{ name: 'select-start', params: {} }">Lub zaznacz gdzie jesteś na liście
    </RouterLink>
  </main>
</template>
