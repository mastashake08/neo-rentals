<template>
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-8">
                <div class="card card-default">
                    <div class="card-header">Rentals</div>

                    <div class="card-body">
                      <ul>
                        <li v-for="rental in rentals">{{rental}}</li>
                      </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        mounted() {
            console.log('Component mounted.')
        },
        data() {
          return {
          rentals : {}

        }
        },
        created(){
          var that = this
          axios.get('/api/rentals').then(function(data){
            that.rentals = data.data.data
          });

        },
        methods:{
          addClaim: function(){
            var that = this
            axios.post('/api/claim',{rental_id:that.selectedRental.id}).then(function(data){
              /*
              Invoke smart contract function to add claim to blockchain
              */
            })
          }
        }
    }
</script>
