<script setup lang="ts">

</script>

<template>
  <main>
    <h2>Nie możesz znaleźć sali?</h2>
    <p>Zeskanuj nabliższy kod QR</p>

    <RouterLink :to="{ name: 'select-start', params: {} }">Wybierz punkt początkowy
    </RouterLink>

    <RouterLink :to="{ name: 'scan-qr', params: {} }">Zeskanuj najbliższy kod QR
    </RouterLink>
  </main>
</template>
