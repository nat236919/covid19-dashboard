<template>
    <div id="show-total" class="text-center">
        <h2> Total Data </h2>
        <div class="row">
            <div v-bind:key="value" v-for="(value, index) in total.data">
                <div class="card col border-dark d-flex justify-content-center" style="width: 16rem; margin-left: 5px;">
                    <h4>{{index}}</h4>
                    <div class="card-body"><p class="card-text">{{value}}</p></div>
                </div>
            </div>
        </div>
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
    h4 { text-transform: capitalize; }
    .card { transition: all .2s ease-in-out; }
    .card:hover { transform: scale(0.9); }
</style>
