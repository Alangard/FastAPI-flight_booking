<template>
  <v-container class="pa-0 ma-0" style="position: relative;">
    <div class="header px-7">
      <div class="mt-4 mb-2"><h4>Hello, @username</h4></div>
      <div class="w-80"><h2>Dreaming of your next trip?</h2></div>
    </div>

    <div class="d-flex flex-row justify-center" style="position: absolute; top: 100px; width: 100vw;">
          <Main></Main>
          <!-- <SearchResult></SearchResult> -->

    </div>    

  </v-container>


</template>

<script>
import Main from "@/pages/Main.vue"
import SearchResult from "@/pages/SearchResult.vue"
  export default {
    components: {
      Main,
      SearchResult
    },
  }
</script>

<style lang='css' scoped>

.header{
  position: absolute;
  z-index: 0;
  width: 100vw;
  height: 240px;
  background-color: #d1ecf3;
}

.city_container{
  position: relative;
}

.v-picker {
  max-width: none !important;
}
</style>