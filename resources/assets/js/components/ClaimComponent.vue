<template>
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-8">
                <div class="card card-default">
                    <div class="card-header">My Wallet</div>

                    <div class="card-body">
                        <b>Your Wallet Address: {{address}}</b>
                        <br>
                        <b>Balance: {{balance}}</b>
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
          rentals : [],
          description:"",
          selectedRental: {},
          scriptBuilder: {}

        }
        },
        created(){
          this.scriptBuilder = Neon.default.create.scriptBuilder()

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
