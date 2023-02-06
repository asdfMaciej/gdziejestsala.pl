<script setup lang="ts">
import router from '@/router/index';
import { computed, ref, inject } from 'vue';

const showBack = computed(() => window.history.length > 1);
</script>

<template>
    <div @click="router.go(-1)">
        <slot>
            <button class="secondary" v-if="showBack">Wróć</button>
        </slot>
    </div>
</template>

<style scoped>

</style>
