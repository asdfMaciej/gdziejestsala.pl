<script setup lang="ts">
import type { Image } from '@/api/models';


const props = defineProps<{
    images: Image[]
}>();


</script>

<template>
    <div class="gallery">
        <picture v-for="image in images">
            <img :src="image.url" :height="image.height" :width="image.width">
        </picture>
    </div>
</template>

<style scoped>
img {
    width: 400px;
    max-width: 100%;
    height: auto;
}

.gallery {
    display: flex;
    flex-wrap: wrap;
}
</style>
