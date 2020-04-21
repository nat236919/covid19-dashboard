<template>
    <div id="show-total">
        <h2> Total Data </h2>
        <li v-bind:key="value" v-for="(value, index) in total.data">
             {{index}} {{value}}
        </li>
    </div>
</template>

<script>
export default {
    data() {
        return {
            total: null
        }
    },
    methods: {

    },
    created() {
        this.$http.get('https://covid2019-api.herokuapp.com/v2/total')
            .then(function(data){
                this.total = data.data;
            })
    }
}
</script>

<style scoped>
</style>
