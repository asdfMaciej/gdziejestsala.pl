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
    <section>
        <h2>Zeskanuj nabliższy kod QR</h2>

        <QRCodeScanner @match="onMatch"></QRCodeScanner>

        <RouterLink :to="{ name: 'select-start', params: {} }">Lub wybierz punkt początkowy
        </RouterLink>
    </section>
</template>
