<template>
    <div>
        <!-- Header -->
        <div>
            <div class="jumbotron jumbotron-fluid">
            <div class="container">
                <h1 class="display-4">Dashboard (Test)</h1>
                <p class="lead">This is a modified jumbotron that occupies the entire horizontal space of its parent.</p>
            </div>
            </div>
        </div>
        <!-- Data -->
        <div class="container">
            <show-total />
            <show-timeseries />
            <show-current />
            <show-randomchart />
        </div>
    </div>
</template>

<script>
import showTotal from './Total.vue'
import showCurrent from './Current.vue'
import showTimeSeries from './TimeSeries.vue'
import showRandomChart from './RandomChart.vue'

export default {
    name: "Dashboard",
    components: {
        'show-total': showTotal,
        'show-current': showCurrent,
        'show-timeseries': showTimeSeries,
        'show-randomchart': showRandomChart
    }
}
</script>

<style scoped>
</style>