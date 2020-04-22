<template>
    <div id="show-total">
        <h2> Current Data </h2>
        {{current.data}}
    </div>
</template>

<script>
export default {
    data() {
        return {
            current: null
        }
    },
    methods: {

    },
    created() {
        this.$http.get('https://covid2019-api.herokuapp.com/v2/current')
                    .then(function(data){
                        this.current = data.data;
                    })
    }
}
</script>

<style scoped>
</style>
