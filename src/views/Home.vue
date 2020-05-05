<template>
<div>
  <MergeHeader />
  <div class="home">
    <AboutUs />
  </div>
</div>
</template>

<script>
// @ is an alias to /src
import MergeHeader from '@/components/MergeHeader.vue'
import AboutUs from '@/components/AboutUs.vue'

export default {
  name: 'Home',
  components: {
    MergeHeader,
    AboutUs
  }
}
</script>
