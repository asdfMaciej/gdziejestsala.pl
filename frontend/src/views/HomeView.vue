<script setup lang="ts">

</script>

<template>
  <section class="homepage">
    <h1>Nie możesz znaleźć sali?</h1>
    <article class="boxes">

      <div class="box box--select-start">
        <RouterLink :to="{ name: 'select-start', params: {} }">
          Wybierz punkt początkowy
        </RouterLink>
      </div>

      <div class="box box--scan-qr">
        <RouterLink :to="{ name: 'scan-qr', params: {} }">
          Zeskanuj najbliższy kod QR
        </RouterLink>
      </div>

    </article>
  </section>
</template>

<style  scoped lang="scss">
.boxes {
  display: flex;
  gap: var(--px-container-padding);
  justify-content: space-evenly;
  flex-wrap: wrap;

  a {
    text-decoration: none;
    font-size: 1.5em;
    font-weight: bold;
    color: var(--hex-white);

    display: flex;
    width: 100%;
    height: 100%;
    align-items: center;
    justify-content: center;

    padding: 10px;
    background: var(--hex-key-a50);
    text-shadow: 1px 2px 0px black;
    border-radius: 15px;
  }
}

.box {
  flex: 1 0 100%;
  border-radius: 15px;
  aspect-ratio: 4/3;

  display: flex;
  align-items: center;
  justify-content: center;

  line-height: 1.3;

  background-size: cover;
  background-position-x: 80%;

  &--scan-qr {
    background-image: url("@/assets/scanning-qr-code.jpg");
  }

  &--select-start {
    background-image: url("@/assets/phone-in-hand.jpg");
  }
}
</style>