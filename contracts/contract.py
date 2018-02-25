"""
Testing:

neo> build sc/3-domain.py test 0710 05 True False query ["test.com"]
neo> build sc/3-domain.py test 0710 05 True False register ["test.com","AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y"]
neo> build sc/3-domain.py test 0710 05 True False delete ["test.com"]
neo> build sc/3-domain.py test 0710 05 True False transfer ["test.com","AK2nJJpJr6o664CWJKi1QRXjqeic"]

Importing:

neo> import contract sc/3-domain.avm 0710 05 True False
neo> contract search ...

Using:

neo> testinvoke 5030694901a527908ab0a1494670109e7b85e3e4 query ["test.com"]
neo> testinvoke 5030694901a527908ab0a1494670109e7b85e3e4 register ["test.com","AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y"]
neo> testinvoke 5030694901a527908ab0a1494670109e7b85e3e4 delete ["test.com"]
neo> testinvoke 5030694901a527908ab0a1494670109e7b85e3e4 transfer ["test.com","AZ9Bmz6qmboZ4ry1z8p2KF3ftyA2ckJAym"]
"""
from boa.blockchain.vm.Neo.Runtime import Log, Notify
from boa.blockchain.vm.Neo.Runtime import CheckWitness
from boa.blockchain.vm.Neo.Storage import GetContext, Get, Put, Delete
from boa.code.builtins import concat
import json


def Main(operation, args):
    nargs = len(args)
    if nargs == 0:
        print("No renter address given")
        return 0

    if operation == 'query':
        renter_wallet_address = args[0]
        return QueryRenter(renter_wallet_address)

    elif operation == 'delete':
        renter_wallet_address = args[0]
        return DeleteRenter(renter_wallet_address)

    elif operation == 'register':
        if nargs < 2:
            print("required arguments: [renter_wallet_address] [owner]")
            return 0
        renter_wallet_address = args[0]
        owner = args[1]
        return RegisterRenter(renter_wallet_address, owner)

    elif operation == 'transfer':
        if nargs < 2:
            print("required arguments: [renter_wallet_address] [to_address]")
            return 0
        renter_wallet_address = args[0]
        to_address = args[1]
        return TransferRenter(renter_wallet_address, to_address)

    elif operation == 'add_payment':
        if nargs < 2:
            print("required arguments: [renter_wallet_address] [property_address]")
            return 0
        renter_wallet_address = args[0]
        property_address = args[1]
        return AddPayment(renter_wallet_address, property_address)

    elif operation == 'add_late_payment':
        if nargs < 2:
            print("required arguments: [renter_wallet_address] [property_address]")
            return 0
        renter_wallet_address = args[0]
        property_address = args[1]
        return AddLatePayment(renter_wallet_address,property_address)

    elif operation == 'add_eviction':
        if nargs < 2:
            print("required arguments: [renter_wallet_address] [property_address]")
            return 0
        renter_wallet_address = args[0]
        property_address = args[1]
        return AddEviction(renter_wallet_address,property_address)

    elif operation == 'should_rent_query':
        if nargs < 2:
            print("required arguments: [renter_wallet_address] [property_address]")
            return 0
        renter_wallet_address = args[0]
        property_address = args[1]
        return ShouldRentQuery(renter_wallet_address,property_address)


def QueryRenter(renter_wallet_address):
    msg = concat("QueryRenter: ", renter_wallet_address)
    Notify(msg)

    context = GetContext()
    owner = Get(context, renter_wallet_address)
    if not owner:
        Notify("Renter is not yet registered")
        return False

    Notify(owner)
    return owner

def ShouldRentQuery(renter_wallet_address,property_address):
    msg = concat("ShouldRentQuery: ", renter_wallet_address)
    Notify(msg)

    context = GetContext()
    renter = Get(context, renter_wallet_address)
    if not renter:
        Notify("Renter is not yet registered")
        return False
    else:
        renter = json.loads(renter)

    Notify(owner)
    return owner

def RegisterRenter(renter_wallet_address, owner):
    msg = concat("RegisterRenter: ", renter_wallet_address)
    Notify(msg)

    if not CheckWitness(owner):
        Notify("Owner argument is not the same as the sender")
        return False

    context = GetContext()
    exists = Get(context, renter_wallet_address)
    if exists:
        msg = concat("Renter: ", exists)
        Notify(msg)
        return False

    Put(context, renter_wallet_address, owner)
    return True

def LogLatePayment(renter_wallet_address, info):
    context = GetContext()
    Put(context, renter_wallet_address, info)
    return True


def TransferRenter(renter_wallet_address, to_address):
    msg = concat("TransferRenter: ", renter_wallet_address)
    Notify(msg)

    context = GetContext()
    owner = Get(context, renter_wallet_address)
    if not owner:
        Notify("Domain is not yet registered")
        return False

    if not CheckWitness(owner):
        Notify("Sender is not the owner, cannot transfer")
        return False

    if not len(to_address) != 34:
        Notify("Invalid new owner address. Must be exactly 34 characters")
        return False

    Put(context, renter_wallet_address, to_address)
    return True


def DeleteRenter(renter_wallet_address):
    msg = concat("DeleteRenter: ", renter_wallet_address)
    Notify(msg)

    context = GetContext()
    owner = Get(context, renter_wallet_address)
    if not owner:
        Notify("Domain is not yet registered")
        return False

    if not CheckWitness(owner):
        Notify("Sender is not the owner, cannot transfer")
        return False

    Delete(context, renter_wallet_address)
    return True
