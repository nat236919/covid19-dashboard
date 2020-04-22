<template>
    <div id="show-total">
        <h2> TimeSeries </h2>
        {{timeseries.data}}
    </div>
</template>

<script>
export default {
    data() {
        return {
            timeseries: null
        }
    },
    methods: {

    },
    created() {
        this.$http.get('https://covid2019-api.herokuapp.com/v2/timeseries/global')
            .then(function(data){
                this.timeseries = data.data;
            })
    }
}
</script>

<style scoped>
</style>
