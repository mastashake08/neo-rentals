<template>
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-8">
                <div class="card card-default">
                    <div class="card-header">Rentals</div>

                    <div class="card-body">
                      <ul>
                        <li v-for="rental in rentals">
                          <span><img width="640" height="640" class="img img-responsive img-rounded" :src="rental.photo"> {{rental.address}} {{rental.city}} {{rental.state}} {{rental.zip}}
                            <br><button class="btn btn-success" v-on:click="promptInquiry()">Inquire</button></span></li><br>
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
          },
          promptInquiry: function(){
            confirm('Inquire about property?')
            // Need to invokeFunction for inquiry function
            alert('Inquiry has been submitted, results will be sent to your email!')
          }
        }
    }
</script>
