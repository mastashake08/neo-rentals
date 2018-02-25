<template>
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-8">
                <div class="card card-default">
                    <div class="card-header">My Wallet</div>

                    <div class="card-body">
                        <b>Your Wallet Address: {{address}}</b>
                        <br>
                        <b>Balance: </b>
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
          privateKey : null,
          wif: null,
          neoAccount: {},
          publicKey: null,
          address: null,
          walletAccount: {},
          balance: ""

        }
        },
        created(){
          var that = this;
          axios.get('/api/me').then(function(data){
            if(data.wallet = null){
              that.createNeoAccount();
            }
            else{
              that.privateKey = data.privateKey;
              that.wif = data.wif;
              that.loadAccount();
            }
          })


        },
        methods:{
          createNeoAccount: function(){
            this.privateKey = Neon.default.create.privateKey();

            this.wif = Neon.default.get.WIFFromPrivateKey(this.privateKey)
            this.neoAccount = Neon.default.create.account(this.privateKey)
            this.publicKey = this.neoAccount.publicKey
            this.address = this.neoAccount.address
            this.walletAccount = new Neon.wallet.Account(this.privateKey)
            /*
            // Encryption / Decryption
            const encrypted = Neon.encrypt.privateKey(privateKey, 'myPassword')
            const decrypted = Neon.decrypt.privateKey(encrypted, 'myPassword')

            // Verify keys
            Neon.is.wif(wif) // true
            Neon.is.publicKey('randomphrase') // false

            // Transaction signing
            const signature = Neon.create.signature(tx, privateKey)
            */
            this.getBalance()

          },
          loadAccount: function(){
            this.neoAccount = Neon.default.create.account(this.privateKey)
            //this.wif = Neon.default.get.WIFFromPrivateKey(this.privateKey)
            this.publicKey = this.neoAccount.publicKey
            this.address = this.neoAccount.address
            this.walletAccount = new Neon.wallet.Account(this.privateKey)
            this.getBalance()



          },
          getBalance: function(){
            this.balance =  new Neon.wallet.Balance({net: 'TestNet', address: this.address})
          }
        }
    }
</script>
