from tartiflette import Resolver, Engine
from tartiflette_asgi import TartifletteApp
from src.utils.env import initEnvDatabase
from src.utils.database import connectDatabase

def startGraphqlServer() :
    # Specify the database connection details
    db_info : dict = initEnvDatabase()
    # Connect to the database
    dbConnection = connectDatabase(db_info["host"][0], db_info["port"][0], db_info["database"][0], db_info["user"][0], db_info["password"])

    sdl = '''
    schema {
        query: query_root
        mutation: mutation_root
        subscription: subscription_root
        }

        """whether this query should be cached (Hasura Cloud only)"""
        directive @cached(
        """measured in seconds"""
        ttl: Int! = 60

        """refresh the cache entry"""
        refresh: Boolean! = false
        ) on QUERY

        """
        Boolean expression to compare columns of type "Boolean". All fields are combined with logical 'AND'.
        """
        input Boolean_comparison_exp {
        _eq: Boolean
        _gt: Boolean
        _gte: Boolean
        _in: [Boolean!]
        _is_null: Boolean
        _lt: Boolean
        _lte: Boolean
        _neq: Boolean
        _nin: [Boolean!]
        }

        """
        Boolean expression to compare columns of type "Int". All fields are combined with logical 'AND'.
        """
        input Int_comparison_exp {
        _eq: Int
        _gt: Int
        _gte: Int
        _in: [Int!]
        _is_null: Boolean
        _lt: Int
        _lte: Int
        _neq: Int
        _nin: [Int!]
        }

        """
        Boolean expression to compare columns of type "String". All fields are combined with logical 'AND'.
        """
        input String_comparison_exp {
        _eq: String
        _gt: String
        _gte: String

        """does the column match the given case-insensitive pattern"""
        _ilike: String
        _in: [String!]

        """
        does the column match the given POSIX regular expression, case insensitive
        """
        _iregex: String
        _is_null: Boolean

        """does the column match the given pattern"""
        _like: String
        _lt: String
        _lte: String
        _neq: String

        """does the column NOT match the given case-insensitive pattern"""
        _nilike: String
        _nin: [String!]

        """
        does the column NOT match the given POSIX regular expression, case insensitive
        """
        _niregex: String

        """does the column NOT match the given pattern"""
        _nlike: String

        """
        does the column NOT match the given POSIX regular expression, case sensitive
        """
        _nregex: String

        """does the column NOT match the given SQL regular expression"""
        _nsimilar: String

        """
        does the column match the given POSIX regular expression, case sensitive
        """
        _regex: String

        """does the column match the given SQL regular expression"""
        _similar: String
        }

        """
        columns and relationships of "contract_dex_operations"
        """
        type contract_dex_operations {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        block: String
        counter: Int
        errors: String
        eventscount: Int
        gaslimit: Int
        gasused: Int
        hash: String
        hasInternals: Boolean
        id: Int!
        initiator: String
        level: Int
        nonce: Int
        parameter: String
        sender: String
        sendercodehash: Int
        status: String
        storagefee: Int
        storagelimit: Int
        storageused: Int
        target: String
        targetcodehash: Int
        timestamp: Int
        tokentransferscount: Int
        type: String
        }

        """
        aggregated selection of "contract_dex_operations"
        """
        type contract_dex_operations_aggregate {
        aggregate: contract_dex_operations_aggregate_fields
        nodes: [contract_dex_operations!]!
        }

        """
        aggregate fields of "contract_dex_operations"
        """
        type contract_dex_operations_aggregate_fields {
        avg: contract_dex_operations_avg_fields
        count(columns: [contract_dex_operations_select_column!], distinct: Boolean): Int!
        max: contract_dex_operations_max_fields
        min: contract_dex_operations_min_fields
        stddev: contract_dex_operations_stddev_fields
        stddev_pop: contract_dex_operations_stddev_pop_fields
        stddev_samp: contract_dex_operations_stddev_samp_fields
        sum: contract_dex_operations_sum_fields
        var_pop: contract_dex_operations_var_pop_fields
        var_samp: contract_dex_operations_var_samp_fields
        variance: contract_dex_operations_variance_fields
        }

        """aggregate avg on columns"""
        type contract_dex_operations_avg_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """
        Boolean expression to filter rows from the table "contract_dex_operations". All fields are combined with a logical 'AND'.
        """
        input contract_dex_operations_bool_exp {
        _and: [contract_dex_operations_bool_exp!]
        _not: contract_dex_operations_bool_exp
        _or: [contract_dex_operations_bool_exp!]
        allocationfee: Int_comparison_exp
        amount: Int_comparison_exp
        bakerfee: Int_comparison_exp
        block: String_comparison_exp
        counter: Int_comparison_exp
        errors: String_comparison_exp
        eventscount: Int_comparison_exp
        gaslimit: Int_comparison_exp
        gasused: Int_comparison_exp
        hash: String_comparison_exp
        hasInternals: Boolean_comparison_exp
        id: Int_comparison_exp
        initiator: String_comparison_exp
        level: Int_comparison_exp
        nonce: Int_comparison_exp
        parameter: String_comparison_exp
        sender: String_comparison_exp
        sendercodehash: Int_comparison_exp
        status: String_comparison_exp
        storagefee: Int_comparison_exp
        storagelimit: Int_comparison_exp
        storageused: Int_comparison_exp
        target: String_comparison_exp
        targetcodehash: Int_comparison_exp
        timestamp: Int_comparison_exp
        tokentransferscount: Int_comparison_exp
        type: String_comparison_exp
        }

        """
        unique or primary key constraInts on table "contract_dex_operations"
        """
        enum contract_dex_operations_constraInt {
        """
        unique or primary key constraInt on columns "id"
        """
        contract_dex_operations_pkey
        }

        """
        input type for incrementing numeric columns in table "contract_dex_operations"
        """
        input contract_dex_operations_inc_input {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        counter: Int
        eventscount: Int
        gaslimit: Int
        gasused: Int
        id: Int
        level: Int
        nonce: Int
        sendercodehash: Int
        storagefee: Int
        storagelimit: Int
        storageused: Int
        targetcodehash: Int
        tokentransferscount: Int
        }

        """
        input type for inserting data Into table "contract_dex_operations"
        """
        input contract_dex_operations_insert_input {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        block: String
        counter: Int
        errors: String
        eventscount: Int
        gaslimit: Int
        gasused: Int
        hash: String
        hasInternals: Boolean
        id: Int
        initiator: String
        level: Int
        nonce: Int
        parameter: String
        sender: String
        sendercodehash: Int
        status: String
        storagefee: Int
        storagelimit: Int
        storageused: Int
        target: String
        targetcodehash: Int
        timestamp: Int
        tokentransferscount: Int
        type: String
        }

        """aggregate max on columns"""
        type contract_dex_operations_max_fields {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        block: String
        counter: Int
        errors: String
        eventscount: Int
        gaslimit: Int
        gasused: Int
        hash: String
        id: Int
        initiator: String
        level: Int
        nonce: Int
        parameter: String
        sender: String
        sendercodehash: Int
        status: String
        storagefee: Int
        storagelimit: Int
        storageused: Int
        target: String
        targetcodehash: Int
        timestamp: Int
        tokentransferscount: Int
        type: String
        }

        """aggregate min on columns"""
        type contract_dex_operations_min_fields {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        block: String
        counter: Int
        errors: String
        eventscount: Int
        gaslimit: Int
        gasused: Int
        hash: String
        id: Int
        initiator: String
        level: Int
        nonce: Int
        parameter: String
        sender: String
        sendercodehash: Int
        status: String
        storagefee: Int
        storagelimit: Int
        storageused: Int
        target: String
        targetcodehash: Int
        timestamp: Int
        tokentransferscount: Int
        type: String
        }

        """
        response of any mutation on the table "contract_dex_operations"
        """
        type contract_dex_operations_mutation_response {
        """number of rows affected by the mutation"""
        affected_rows: Int!

        """data from the rows affected by the mutation"""
        returning: [contract_dex_operations!]!
        }

        """
        on_conflict condition type for table "contract_dex_operations"
        """
        input contract_dex_operations_on_conflict {
        constraInt: contract_dex_operations_constraInt!
        update_columns: [contract_dex_operations_update_column!]! = []
        where: contract_dex_operations_bool_exp
        }

        """Ordering options when selecting data from "contract_dex_operations"."""
        input contract_dex_operations_order_by {
        allocationfee: order_by
        amount: order_by
        bakerfee: order_by
        block: order_by
        counter: order_by
        errors: order_by
        eventscount: order_by
        gaslimit: order_by
        gasused: order_by
        hash: order_by
        hasInternals: order_by
        id: order_by
        initiator: order_by
        level: order_by
        nonce: order_by
        parameter: order_by
        sender: order_by
        sendercodehash: order_by
        status: order_by
        storagefee: order_by
        storagelimit: order_by
        storageused: order_by
        target: order_by
        targetcodehash: order_by
        timestamp: order_by
        tokentransferscount: order_by
        type: order_by
        }

        """primary key columns input for table: contract_dex_operations"""
        input contract_dex_operations_pk_columns_input {
        id: Int!
        }

        """
        select columns of table "contract_dex_operations"
        """
        enum contract_dex_operations_select_column {
        """column name"""
        allocationfee

        """column name"""
        amount

        """column name"""
        bakerfee

        """column name"""
        block

        """column name"""
        counter

        """column name"""
        errors

        """column name"""
        eventscount

        """column name"""
        gaslimit

        """column name"""
        gasused

        """column name"""
        hash

        """column name"""
        hasInternals

        """column name"""
        id

        """column name"""
        initiator

        """column name"""
        level

        """column name"""
        nonce

        """column name"""
        parameter

        """column name"""
        sender

        """column name"""
        sendercodehash

        """column name"""
        status

        """column name"""
        storagefee

        """column name"""
        storagelimit

        """column name"""
        storageused

        """column name"""
        target

        """column name"""
        targetcodehash

        """column name"""
        timestamp

        """column name"""
        tokentransferscount

        """column name"""
        type
        }

        """
        input type for updating data in table "contract_dex_operations"
        """
        input contract_dex_operations_set_input {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        block: String
        counter: Int
        errors: String
        eventscount: Int
        gaslimit: Int
        gasused: Int
        hash: String
        hasInternals: Boolean
        id: Int
        initiator: String
        level: Int
        nonce: Int
        parameter: String
        sender: String
        sendercodehash: Int
        status: String
        storagefee: Int
        storagelimit: Int
        storageused: Int
        target: String
        targetcodehash: Int
        timestamp: Int
        tokentransferscount: Int
        type: String
        }

        """aggregate stddev on columns"""
        type contract_dex_operations_stddev_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """aggregate stddev_pop on columns"""
        type contract_dex_operations_stddev_pop_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """aggregate stddev_samp on columns"""
        type contract_dex_operations_stddev_samp_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """
        Streaming cursor of the table "contract_dex_operations"
        """
        input contract_dex_operations_stream_cursor_input {
        """Stream column input with initial value"""
        initial_value: contract_dex_operations_stream_cursor_value_input!

        """cursor ordering"""
        ordering: cursor_ordering
        }

        """Initial value of the column from where the streaming should start"""
        input contract_dex_operations_stream_cursor_value_input {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        block: String
        counter: Int
        errors: String
        eventscount: Int
        gaslimit: Int
        gasused: Int
        hash: String
        hasInternals: Boolean
        id: Int
        initiator: String
        level: Int
        nonce: Int
        parameter: String
        sender: String
        sendercodehash: Int
        status: String
        storagefee: Int
        storagelimit: Int
        storageused: Int
        target: String
        targetcodehash: Int
        timestamp: Int
        tokentransferscount: Int
        type: String
        }

        """aggregate sum on columns"""
        type contract_dex_operations_sum_fields {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        counter: Int
        eventscount: Int
        gaslimit: Int
        gasused: Int
        id: Int
        level: Int
        nonce: Int
        sendercodehash: Int
        storagefee: Int
        storagelimit: Int
        storageused: Int
        targetcodehash: Int
        tokentransferscount: Int
        }

        """
        update columns of table "contract_dex_operations"
        """
        enum contract_dex_operations_update_column {
        """column name"""
        allocationfee

        """column name"""
        amount

        """column name"""
        bakerfee

        """column name"""
        block

        """column name"""
        counter

        """column name"""
        errors

        """column name"""
        eventscount

        """column name"""
        gaslimit

        """column name"""
        gasused

        """column name"""
        hash

        """column name"""
        hasInternals

        """column name"""
        id

        """column name"""
        initiator

        """column name"""
        level

        """column name"""
        nonce

        """column name"""
        parameter

        """column name"""
        sender

        """column name"""
        sendercodehash

        """column name"""
        status

        """column name"""
        storagefee

        """column name"""
        storagelimit

        """column name"""
        storageused

        """column name"""
        target

        """column name"""
        targetcodehash

        """column name"""
        timestamp

        """column name"""
        tokentransferscount

        """column name"""
        type
        }

        input contract_dex_operations_updates {
        """increments the numeric columns with given value of the filtered values"""
        _inc: contract_dex_operations_inc_input

        """sets the columns of the filtered rows to the given values"""
        _set: contract_dex_operations_set_input

        """filter the rows which have to be updated"""
        where: contract_dex_operations_bool_exp!
        }

        """aggregate var_pop on columns"""
        type contract_dex_operations_var_pop_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """aggregate var_samp on columns"""
        type contract_dex_operations_var_samp_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """aggregate variance on columns"""
        type contract_dex_operations_variance_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """
        columns and relationships of "contract_dex_storage"
        """
        type contract_dex_storage {
        freezebaker: Boolean
        history: Int
        id: Int!
        lqtaddress: String
        lqttotal: String
        manager: String
        reserve: String
        selfisupdatingtokenpool: Boolean
        tokenaddress: String
        tokenpool: String
        user_investments: Int
        xtzpool: String
        }

        """
        aggregated selection of "contract_dex_storage"
        """
        type contract_dex_storage_aggregate {
        aggregate: contract_dex_storage_aggregate_fields
        nodes: [contract_dex_storage!]!
        }

        """
        aggregate fields of "contract_dex_storage"
        """
        type contract_dex_storage_aggregate_fields {
        avg: contract_dex_storage_avg_fields
        count(columns: [contract_dex_storage_select_column!], distinct: Boolean): Int!
        max: contract_dex_storage_max_fields
        min: contract_dex_storage_min_fields
        stddev: contract_dex_storage_stddev_fields
        stddev_pop: contract_dex_storage_stddev_pop_fields
        stddev_samp: contract_dex_storage_stddev_samp_fields
        sum: contract_dex_storage_sum_fields
        var_pop: contract_dex_storage_var_pop_fields
        var_samp: contract_dex_storage_var_samp_fields
        variance: contract_dex_storage_variance_fields
        }

        """aggregate avg on columns"""
        type contract_dex_storage_avg_fields {
        history: Float
        id: Float
        user_investments: Float
        }

        """
        Boolean expression to filter rows from the table "contract_dex_storage". All fields are combined with a logical 'AND'.
        """
        input contract_dex_storage_bool_exp {
        _and: [contract_dex_storage_bool_exp!]
        _not: contract_dex_storage_bool_exp
        _or: [contract_dex_storage_bool_exp!]
        freezebaker: Boolean_comparison_exp
        history: Int_comparison_exp
        id: Int_comparison_exp
        lqtaddress: String_comparison_exp
        lqttotal: String_comparison_exp
        manager: String_comparison_exp
        reserve: String_comparison_exp
        selfisupdatingtokenpool: Boolean_comparison_exp
        tokenaddress: String_comparison_exp
        tokenpool: String_comparison_exp
        user_investments: Int_comparison_exp
        xtzpool: String_comparison_exp
        }

        """
        unique or primary key constraInts on table "contract_dex_storage"
        """
        enum contract_dex_storage_constraInt {
        """
        unique or primary key constraInt on columns "id"
        """
        contract_dex_storage_pkey
        }

        """
        input type for incrementing numeric columns in table "contract_dex_storage"
        """
        input contract_dex_storage_inc_input {
        history: Int
        id: Int
        user_investments: Int
        }

        """
        input type for inserting data Into table "contract_dex_storage"
        """
        input contract_dex_storage_insert_input {
        freezebaker: Boolean
        history: Int
        id: Int
        lqtaddress: String
        lqttotal: String
        manager: String
        reserve: String
        selfisupdatingtokenpool: Boolean
        tokenaddress: String
        tokenpool: String
        user_investments: Int
        xtzpool: String
        }

        """aggregate max on columns"""
        type contract_dex_storage_max_fields {
        history: Int
        id: Int
        lqtaddress: String
        lqttotal: String
        manager: String
        reserve: String
        tokenaddress: String
        tokenpool: String
        user_investments: Int
        xtzpool: String
        }

        """aggregate min on columns"""
        type contract_dex_storage_min_fields {
        history: Int
        id: Int
        lqtaddress: String
        lqttotal: String
        manager: String
        reserve: String
        tokenaddress: String
        tokenpool: String
        user_investments: Int
        xtzpool: String
        }

        """
        response of any mutation on the table "contract_dex_storage"
        """
        type contract_dex_storage_mutation_response {
        """number of rows affected by the mutation"""
        affected_rows: Int!

        """data from the rows affected by the mutation"""
        returning: [contract_dex_storage!]!
        }

        """
        on_conflict condition type for table "contract_dex_storage"
        """
        input contract_dex_storage_on_conflict {
        constraInt: contract_dex_storage_constraInt!
        update_columns: [contract_dex_storage_update_column!]! = []
        where: contract_dex_storage_bool_exp
        }

        """Ordering options when selecting data from "contract_dex_storage"."""
        input contract_dex_storage_order_by {
        freezebaker: order_by
        history: order_by
        id: order_by
        lqtaddress: order_by
        lqttotal: order_by
        manager: order_by
        reserve: order_by
        selfisupdatingtokenpool: order_by
        tokenaddress: order_by
        tokenpool: order_by
        user_investments: order_by
        xtzpool: order_by
        }

        """primary key columns input for table: contract_dex_storage"""
        input contract_dex_storage_pk_columns_input {
        id: Int!
        }

        """
        select columns of table "contract_dex_storage"
        """
        enum contract_dex_storage_select_column {
        """column name"""
        freezebaker

        """column name"""
        history

        """column name"""
        id

        """column name"""
        lqtaddress

        """column name"""
        lqttotal

        """column name"""
        manager

        """column name"""
        reserve

        """column name"""
        selfisupdatingtokenpool

        """column name"""
        tokenaddress

        """column name"""
        tokenpool

        """column name"""
        user_investments

        """column name"""
        xtzpool
        }

        """
        input type for updating data in table "contract_dex_storage"
        """
        input contract_dex_storage_set_input {
        freezebaker: Boolean
        history: Int
        id: Int
        lqtaddress: String
        lqttotal: String
        manager: String
        reserve: String
        selfisupdatingtokenpool: Boolean
        tokenaddress: String
        tokenpool: String
        user_investments: Int
        xtzpool: String
        }

        """aggregate stddev on columns"""
        type contract_dex_storage_stddev_fields {
        history: Float
        id: Float
        user_investments: Float
        }

        """aggregate stddev_pop on columns"""
        type contract_dex_storage_stddev_pop_fields {
        history: Float
        id: Float
        user_investments: Float
        }

        """aggregate stddev_samp on columns"""
        type contract_dex_storage_stddev_samp_fields {
        history: Float
        id: Float
        user_investments: Float
        }

        """
        Streaming cursor of the table "contract_dex_storage"
        """
        input contract_dex_storage_stream_cursor_input {
        """Stream column input with initial value"""
        initial_value: contract_dex_storage_stream_cursor_value_input!

        """cursor ordering"""
        ordering: cursor_ordering
        }

        """Initial value of the column from where the streaming should start"""
        input contract_dex_storage_stream_cursor_value_input {
        freezebaker: Boolean
        history: Int
        id: Int
        lqtaddress: String
        lqttotal: String
        manager: String
        reserve: String
        selfisupdatingtokenpool: Boolean
        tokenaddress: String
        tokenpool: String
        user_investments: Int
        xtzpool: String
        }

        """aggregate sum on columns"""
        type contract_dex_storage_sum_fields {
        history: Int
        id: Int
        user_investments: Int
        }

        """
        update columns of table "contract_dex_storage"
        """
        enum contract_dex_storage_update_column {
        """column name"""
        freezebaker

        """column name"""
        history

        """column name"""
        id

        """column name"""
        lqtaddress

        """column name"""
        lqttotal

        """column name"""
        manager

        """column name"""
        reserve

        """column name"""
        selfisupdatingtokenpool

        """column name"""
        tokenaddress

        """column name"""
        tokenpool

        """column name"""
        user_investments

        """column name"""
        xtzpool
        }

        input contract_dex_storage_updates {
        """increments the numeric columns with given value of the filtered values"""
        _inc: contract_dex_storage_inc_input

        """sets the columns of the filtered rows to the given values"""
        _set: contract_dex_storage_set_input

        """filter the rows which have to be updated"""
        where: contract_dex_storage_bool_exp!
        }

        """aggregate var_pop on columns"""
        type contract_dex_storage_var_pop_fields {
        history: Float
        id: Float
        user_investments: Float
        }

        """aggregate var_samp on columns"""
        type contract_dex_storage_var_samp_fields {
        history: Float
        id: Float
        user_investments: Float
        }

        """aggregate variance on columns"""
        type contract_dex_storage_variance_fields {
        history: Float
        id: Float
        user_investments: Float
        }

        """
        columns and relationships of "contract_factory_doga_operations"
        """
        type contract_factory_doga_operations {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        block: String
        counter: Int
        errors: String
        eventscount: Int
        gaslimit: Int
        gasused: Int
        hash: String
        hasInternals: Boolean
        id: Int!
        initiator: String
        level: Int
        nonce: Int
        parameter: String
        sender: String
        sendercodehash: Int
        status: String
        storagefee: Int
        storagelimit: Int
        storageused: Int
        target: String
        targetcodehash: Int
        timestamp: Int
        tokentransferscount: Int
        type: String
        }

        """
        aggregated selection of "contract_factory_doga_operations"
        """
        type contract_factory_doga_operations_aggregate {
        aggregate: contract_factory_doga_operations_aggregate_fields
        nodes: [contract_factory_doga_operations!]!
        }

        """
        aggregate fields of "contract_factory_doga_operations"
        """
        type contract_factory_doga_operations_aggregate_fields {
        avg: contract_factory_doga_operations_avg_fields
        count(columns: [contract_factory_doga_operations_select_column!], distinct: Boolean): Int!
        max: contract_factory_doga_operations_max_fields
        min: contract_factory_doga_operations_min_fields
        stddev: contract_factory_doga_operations_stddev_fields
        stddev_pop: contract_factory_doga_operations_stddev_pop_fields
        stddev_samp: contract_factory_doga_operations_stddev_samp_fields
        sum: contract_factory_doga_operations_sum_fields
        var_pop: contract_factory_doga_operations_var_pop_fields
        var_samp: contract_factory_doga_operations_var_samp_fields
        variance: contract_factory_doga_operations_variance_fields
        }

        """aggregate avg on columns"""
        type contract_factory_doga_operations_avg_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """
        Boolean expression to filter rows from the table "contract_factory_doga_operations". All fields are combined with a logical 'AND'.
        """
        input contract_factory_doga_operations_bool_exp {
        _and: [contract_factory_doga_operations_bool_exp!]
        _not: contract_factory_doga_operations_bool_exp
        _or: [contract_factory_doga_operations_bool_exp!]
        allocationfee: Int_comparison_exp
        amount: Int_comparison_exp
        bakerfee: Int_comparison_exp
        block: String_comparison_exp
        counter: Int_comparison_exp
        errors: String_comparison_exp
        eventscount: Int_comparison_exp
        gaslimit: Int_comparison_exp
        gasused: Int_comparison_exp
        hash: String_comparison_exp
        hasInternals: Boolean_comparison_exp
        id: Int_comparison_exp
        initiator: String_comparison_exp
        level: Int_comparison_exp
        nonce: Int_comparison_exp
        parameter: String_comparison_exp
        sender: String_comparison_exp
        sendercodehash: Int_comparison_exp
        status: String_comparison_exp
        storagefee: Int_comparison_exp
        storagelimit: Int_comparison_exp
        storageused: Int_comparison_exp
        target: String_comparison_exp
        targetcodehash: Int_comparison_exp
        timestamp: Int_comparison_exp
        tokentransferscount: Int_comparison_exp
        type: String_comparison_exp
        }

        """
        unique or primary key constraInts on table "contract_factory_doga_operations"
        """
        enum contract_factory_doga_operations_constraInt {
        """
        unique or primary key constraInt on columns "id"
        """
        contract_factory_doga_operations_pkey
        }

        """
        input type for incrementing numeric columns in table "contract_factory_doga_operations"
        """
        input contract_factory_doga_operations_inc_input {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        counter: Int
        eventscount: Int
        gaslimit: Int
        gasused: Int
        id: Int
        level: Int
        nonce: Int
        sendercodehash: Int
        storagefee: Int
        storagelimit: Int
        storageused: Int
        targetcodehash: Int
        tokentransferscount: Int
        }

        """
        input type for inserting data Into table "contract_factory_doga_operations"
        """
        input contract_factory_doga_operations_insert_input {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        block: String
        counter: Int
        errors: String
        eventscount: Int
        gaslimit: Int
        gasused: Int
        hash: String
        hasInternals: Boolean
        id: Int
        initiator: String
        level: Int
        nonce: Int
        parameter: String
        sender: String
        sendercodehash: Int
        status: String
        storagefee: Int
        storagelimit: Int
        storageused: Int
        target: String
        targetcodehash: Int
        timestamp: Int
        tokentransferscount: Int
        type: String
        }

        """aggregate max on columns"""
        type contract_factory_doga_operations_max_fields {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        block: String
        counter: Int
        errors: String
        eventscount: Int
        gaslimit: Int
        gasused: Int
        hash: String
        id: Int
        initiator: String
        level: Int
        nonce: Int
        parameter: String
        sender: String
        sendercodehash: Int
        status: String
        storagefee: Int
        storagelimit: Int
        storageused: Int
        target: String
        targetcodehash: Int
        timestamp: Int
        tokentransferscount: Int
        type: String
        }

        """aggregate min on columns"""
        type contract_factory_doga_operations_min_fields {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        block: String
        counter: Int
        errors: String
        eventscount: Int
        gaslimit: Int
        gasused: Int
        hash: String
        id: Int
        initiator: String
        level: Int
        nonce: Int
        parameter: String
        sender: String
        sendercodehash: Int
        status: String
        storagefee: Int
        storagelimit: Int
        storageused: Int
        target: String
        targetcodehash: Int
        timestamp: Int
        tokentransferscount: Int
        type: String
        }

        """
        response of any mutation on the table "contract_factory_doga_operations"
        """
        type contract_factory_doga_operations_mutation_response {
        """number of rows affected by the mutation"""
        affected_rows: Int!

        """data from the rows affected by the mutation"""
        returning: [contract_factory_doga_operations!]!
        }

        """
        on_conflict condition type for table "contract_factory_doga_operations"
        """
        input contract_factory_doga_operations_on_conflict {
        constraInt: contract_factory_doga_operations_constraInt!
        update_columns: [contract_factory_doga_operations_update_column!]! = []
        where: contract_factory_doga_operations_bool_exp
        }

        """
        Ordering options when selecting data from "contract_factory_doga_operations".
        """
        input contract_factory_doga_operations_order_by {
        allocationfee: order_by
        amount: order_by
        bakerfee: order_by
        block: order_by
        counter: order_by
        errors: order_by
        eventscount: order_by
        gaslimit: order_by
        gasused: order_by
        hash: order_by
        hasInternals: order_by
        id: order_by
        initiator: order_by
        level: order_by
        nonce: order_by
        parameter: order_by
        sender: order_by
        sendercodehash: order_by
        status: order_by
        storagefee: order_by
        storagelimit: order_by
        storageused: order_by
        target: order_by
        targetcodehash: order_by
        timestamp: order_by
        tokentransferscount: order_by
        type: order_by
        }

        """primary key columns input for table: contract_factory_doga_operations"""
        input contract_factory_doga_operations_pk_columns_input {
        id: Int!
        }

        """
        select columns of table "contract_factory_doga_operations"
        """
        enum contract_factory_doga_operations_select_column {
        """column name"""
        allocationfee

        """column name"""
        amount

        """column name"""
        bakerfee

        """column name"""
        block

        """column name"""
        counter

        """column name"""
        errors

        """column name"""
        eventscount

        """column name"""
        gaslimit

        """column name"""
        gasused

        """column name"""
        hash

        """column name"""
        hasInternals

        """column name"""
        id

        """column name"""
        initiator

        """column name"""
        level

        """column name"""
        nonce

        """column name"""
        parameter

        """column name"""
        sender

        """column name"""
        sendercodehash

        """column name"""
        status

        """column name"""
        storagefee

        """column name"""
        storagelimit

        """column name"""
        storageused

        """column name"""
        target

        """column name"""
        targetcodehash

        """column name"""
        timestamp

        """column name"""
        tokentransferscount

        """column name"""
        type
        }

        """
        input type for updating data in table "contract_factory_doga_operations"
        """
        input contract_factory_doga_operations_set_input {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        block: String
        counter: Int
        errors: String
        eventscount: Int
        gaslimit: Int
        gasused: Int
        hash: String
        hasInternals: Boolean
        id: Int
        initiator: String
        level: Int
        nonce: Int
        parameter: String
        sender: String
        sendercodehash: Int
        status: String
        storagefee: Int
        storagelimit: Int
        storageused: Int
        target: String
        targetcodehash: Int
        timestamp: Int
        tokentransferscount: Int
        type: String
        }

        """aggregate stddev on columns"""
        type contract_factory_doga_operations_stddev_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """aggregate stddev_pop on columns"""
        type contract_factory_doga_operations_stddev_pop_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """aggregate stddev_samp on columns"""
        type contract_factory_doga_operations_stddev_samp_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """
        Streaming cursor of the table "contract_factory_doga_operations"
        """
        input contract_factory_doga_operations_stream_cursor_input {
        """Stream column input with initial value"""
        initial_value: contract_factory_doga_operations_stream_cursor_value_input!

        """cursor ordering"""
        ordering: cursor_ordering
        }

        """Initial value of the column from where the streaming should start"""
        input contract_factory_doga_operations_stream_cursor_value_input {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        block: String
        counter: Int
        errors: String
        eventscount: Int
        gaslimit: Int
        gasused: Int
        hash: String
        hasInternals: Boolean
        id: Int
        initiator: String
        level: Int
        nonce: Int
        parameter: String
        sender: String
        sendercodehash: Int
        status: String
        storagefee: Int
        storagelimit: Int
        storageused: Int
        target: String
        targetcodehash: Int
        timestamp: Int
        tokentransferscount: Int
        type: String
        }

        """aggregate sum on columns"""
        type contract_factory_doga_operations_sum_fields {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        counter: Int
        eventscount: Int
        gaslimit: Int
        gasused: Int
        id: Int
        level: Int
        nonce: Int
        sendercodehash: Int
        storagefee: Int
        storagelimit: Int
        storageused: Int
        targetcodehash: Int
        tokentransferscount: Int
        }

        """
        update columns of table "contract_factory_doga_operations"
        """
        enum contract_factory_doga_operations_update_column {
        """column name"""
        allocationfee

        """column name"""
        amount

        """column name"""
        bakerfee

        """column name"""
        block

        """column name"""
        counter

        """column name"""
        errors

        """column name"""
        eventscount

        """column name"""
        gaslimit

        """column name"""
        gasused

        """column name"""
        hash

        """column name"""
        hasInternals

        """column name"""
        id

        """column name"""
        initiator

        """column name"""
        level

        """column name"""
        nonce

        """column name"""
        parameter

        """column name"""
        sender

        """column name"""
        sendercodehash

        """column name"""
        status

        """column name"""
        storagefee

        """column name"""
        storagelimit

        """column name"""
        storageused

        """column name"""
        target

        """column name"""
        targetcodehash

        """column name"""
        timestamp

        """column name"""
        tokentransferscount

        """column name"""
        type
        }

        input contract_factory_doga_operations_updates {
        """increments the numeric columns with given value of the filtered values"""
        _inc: contract_factory_doga_operations_inc_input

        """sets the columns of the filtered rows to the given values"""
        _set: contract_factory_doga_operations_set_input

        """filter the rows which have to be updated"""
        where: contract_factory_doga_operations_bool_exp!
        }

        """aggregate var_pop on columns"""
        type contract_factory_doga_operations_var_pop_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """aggregate var_samp on columns"""
        type contract_factory_doga_operations_var_samp_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """aggregate variance on columns"""
        type contract_factory_doga_operations_variance_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """
        columns and relationships of "contract_factory_doga_storage"
        """
        type contract_factory_doga_storage {
        counter: Int
        default_metadata: Int
        default_reserve: String
        default_token_metadata: Int
        empty_allowances: Int
        empty_history: Int
        empty_tokens: Int
        empty_user_investments: Int
        id: Int!
        swaps: Int
        token_to_swaps: Int
        }

        """
        aggregated selection of "contract_factory_doga_storage"
        """
        type contract_factory_doga_storage_aggregate {
        aggregate: contract_factory_doga_storage_aggregate_fields
        nodes: [contract_factory_doga_storage!]!
        }

        """
        aggregate fields of "contract_factory_doga_storage"
        """
        type contract_factory_doga_storage_aggregate_fields {
        avg: contract_factory_doga_storage_avg_fields
        count(columns: [contract_factory_doga_storage_select_column!], distinct: Boolean): Int!
        max: contract_factory_doga_storage_max_fields
        min: contract_factory_doga_storage_min_fields
        stddev: contract_factory_doga_storage_stddev_fields
        stddev_pop: contract_factory_doga_storage_stddev_pop_fields
        stddev_samp: contract_factory_doga_storage_stddev_samp_fields
        sum: contract_factory_doga_storage_sum_fields
        var_pop: contract_factory_doga_storage_var_pop_fields
        var_samp: contract_factory_doga_storage_var_samp_fields
        variance: contract_factory_doga_storage_variance_fields
        }

        """aggregate avg on columns"""
        type contract_factory_doga_storage_avg_fields {
        counter: Float
        default_metadata: Float
        default_token_metadata: Float
        empty_allowances: Float
        empty_history: Float
        empty_tokens: Float
        empty_user_investments: Float
        id: Float
        swaps: Float
        token_to_swaps: Float
        }

        """
        Boolean expression to filter rows from the table "contract_factory_doga_storage". All fields are combined with a logical 'AND'.
        """
        input contract_factory_doga_storage_bool_exp {
        _and: [contract_factory_doga_storage_bool_exp!]
        _not: contract_factory_doga_storage_bool_exp
        _or: [contract_factory_doga_storage_bool_exp!]
        counter: Int_comparison_exp
        default_metadata: Int_comparison_exp
        default_reserve: String_comparison_exp
        default_token_metadata: Int_comparison_exp
        empty_allowances: Int_comparison_exp
        empty_history: Int_comparison_exp
        empty_tokens: Int_comparison_exp
        empty_user_investments: Int_comparison_exp
        id: Int_comparison_exp
        swaps: Int_comparison_exp
        token_to_swaps: Int_comparison_exp
        }

        """
        unique or primary key constraInts on table "contract_factory_doga_storage"
        """
        enum contract_factory_doga_storage_constraInt {
        """
        unique or primary key constraInt on columns "id"
        """
        contract_factory_doga_storage_pkey
        }

        """
        input type for incrementing numeric columns in table "contract_factory_doga_storage"
        """
        input contract_factory_doga_storage_inc_input {
        counter: Int
        default_metadata: Int
        default_token_metadata: Int
        empty_allowances: Int
        empty_history: Int
        empty_tokens: Int
        empty_user_investments: Int
        id: Int
        swaps: Int
        token_to_swaps: Int
        }

        """
        input type for inserting data Into table "contract_factory_doga_storage"
        """
        input contract_factory_doga_storage_insert_input {
        counter: Int
        default_metadata: Int
        default_reserve: String
        default_token_metadata: Int
        empty_allowances: Int
        empty_history: Int
        empty_tokens: Int
        empty_user_investments: Int
        id: Int
        swaps: Int
        token_to_swaps: Int
        }

        """aggregate max on columns"""
        type contract_factory_doga_storage_max_fields {
        counter: Int
        default_metadata: Int
        default_reserve: String
        default_token_metadata: Int
        empty_allowances: Int
        empty_history: Int
        empty_tokens: Int
        empty_user_investments: Int
        id: Int
        swaps: Int
        token_to_swaps: Int
        }

        """aggregate min on columns"""
        type contract_factory_doga_storage_min_fields {
        counter: Int
        default_metadata: Int
        default_reserve: String
        default_token_metadata: Int
        empty_allowances: Int
        empty_history: Int
        empty_tokens: Int
        empty_user_investments: Int
        id: Int
        swaps: Int
        token_to_swaps: Int
        }

        """
        response of any mutation on the table "contract_factory_doga_storage"
        """
        type contract_factory_doga_storage_mutation_response {
        """number of rows affected by the mutation"""
        affected_rows: Int!

        """data from the rows affected by the mutation"""
        returning: [contract_factory_doga_storage!]!
        }

        """
        on_conflict condition type for table "contract_factory_doga_storage"
        """
        input contract_factory_doga_storage_on_conflict {
        constraInt: contract_factory_doga_storage_constraInt!
        update_columns: [contract_factory_doga_storage_update_column!]! = []
        where: contract_factory_doga_storage_bool_exp
        }

        """
        Ordering options when selecting data from "contract_factory_doga_storage".
        """
        input contract_factory_doga_storage_order_by {
        counter: order_by
        default_metadata: order_by
        default_reserve: order_by
        default_token_metadata: order_by
        empty_allowances: order_by
        empty_history: order_by
        empty_tokens: order_by
        empty_user_investments: order_by
        id: order_by
        swaps: order_by
        token_to_swaps: order_by
        }

        """primary key columns input for table: contract_factory_doga_storage"""
        input contract_factory_doga_storage_pk_columns_input {
        id: Int!
        }

        """
        select columns of table "contract_factory_doga_storage"
        """
        enum contract_factory_doga_storage_select_column {
        """column name"""
        counter

        """column name"""
        default_metadata

        """column name"""
        default_reserve

        """column name"""
        default_token_metadata

        """column name"""
        empty_allowances

        """column name"""
        empty_history

        """column name"""
        empty_tokens

        """column name"""
        empty_user_investments

        """column name"""
        id

        """column name"""
        swaps

        """column name"""
        token_to_swaps
        }

        """
        input type for updating data in table "contract_factory_doga_storage"
        """
        input contract_factory_doga_storage_set_input {
        counter: Int
        default_metadata: Int
        default_reserve: String
        default_token_metadata: Int
        empty_allowances: Int
        empty_history: Int
        empty_tokens: Int
        empty_user_investments: Int
        id: Int
        swaps: Int
        token_to_swaps: Int
        }

        """aggregate stddev on columns"""
        type contract_factory_doga_storage_stddev_fields {
        counter: Float
        default_metadata: Float
        default_token_metadata: Float
        empty_allowances: Float
        empty_history: Float
        empty_tokens: Float
        empty_user_investments: Float
        id: Float
        swaps: Float
        token_to_swaps: Float
        }

        """aggregate stddev_pop on columns"""
        type contract_factory_doga_storage_stddev_pop_fields {
        counter: Float
        default_metadata: Float
        default_token_metadata: Float
        empty_allowances: Float
        empty_history: Float
        empty_tokens: Float
        empty_user_investments: Float
        id: Float
        swaps: Float
        token_to_swaps: Float
        }

        """aggregate stddev_samp on columns"""
        type contract_factory_doga_storage_stddev_samp_fields {
        counter: Float
        default_metadata: Float
        default_token_metadata: Float
        empty_allowances: Float
        empty_history: Float
        empty_tokens: Float
        empty_user_investments: Float
        id: Float
        swaps: Float
        token_to_swaps: Float
        }

        """
        Streaming cursor of the table "contract_factory_doga_storage"
        """
        input contract_factory_doga_storage_stream_cursor_input {
        """Stream column input with initial value"""
        initial_value: contract_factory_doga_storage_stream_cursor_value_input!

        """cursor ordering"""
        ordering: cursor_ordering
        }

        """Initial value of the column from where the streaming should start"""
        input contract_factory_doga_storage_stream_cursor_value_input {
        counter: Int
        default_metadata: Int
        default_reserve: String
        default_token_metadata: Int
        empty_allowances: Int
        empty_history: Int
        empty_tokens: Int
        empty_user_investments: Int
        id: Int
        swaps: Int
        token_to_swaps: Int
        }

        """aggregate sum on columns"""
        type contract_factory_doga_storage_sum_fields {
        counter: Int
        default_metadata: Int
        default_token_metadata: Int
        empty_allowances: Int
        empty_history: Int
        empty_tokens: Int
        empty_user_investments: Int
        id: Int
        swaps: Int
        token_to_swaps: Int
        }

        """
        update columns of table "contract_factory_doga_storage"
        """
        enum contract_factory_doga_storage_update_column {
        """column name"""
        counter

        """column name"""
        default_metadata

        """column name"""
        default_reserve

        """column name"""
        default_token_metadata

        """column name"""
        empty_allowances

        """column name"""
        empty_history

        """column name"""
        empty_tokens

        """column name"""
        empty_user_investments

        """column name"""
        id

        """column name"""
        swaps

        """column name"""
        token_to_swaps
        }

        input contract_factory_doga_storage_updates {
        """increments the numeric columns with given value of the filtered values"""
        _inc: contract_factory_doga_storage_inc_input

        """sets the columns of the filtered rows to the given values"""
        _set: contract_factory_doga_storage_set_input

        """filter the rows which have to be updated"""
        where: contract_factory_doga_storage_bool_exp!
        }

        """aggregate var_pop on columns"""
        type contract_factory_doga_storage_var_pop_fields {
        counter: Float
        default_metadata: Float
        default_token_metadata: Float
        empty_allowances: Float
        empty_history: Float
        empty_tokens: Float
        empty_user_investments: Float
        id: Float
        swaps: Float
        token_to_swaps: Float
        }

        """aggregate var_samp on columns"""
        type contract_factory_doga_storage_var_samp_fields {
        counter: Float
        default_metadata: Float
        default_token_metadata: Float
        empty_allowances: Float
        empty_history: Float
        empty_tokens: Float
        empty_user_investments: Float
        id: Float
        swaps: Float
        token_to_swaps: Float
        }

        """aggregate variance on columns"""
        type contract_factory_doga_storage_variance_fields {
        counter: Float
        default_metadata: Float
        default_token_metadata: Float
        empty_allowances: Float
        empty_history: Float
        empty_tokens: Float
        empty_user_investments: Float
        id: Float
        swaps: Float
        token_to_swaps: Float
        }

        """
        columns and relationships of "contract_factory_fa12_operations"
        """
        type contract_factory_fa12_operations {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        block: String
        counter: Int
        errors: String
        eventscount: Int
        gaslimit: Int
        gasused: Int
        hash: String
        hasInternals: Boolean
        id: Int!
        initiator: String
        level: Int
        nonce: Int
        parameter: String
        sender: String
        sendercodehash: Int
        status: String
        storagefee: Int
        storagelimit: Int
        storageused: Int
        target: String
        targetcodehash: Int
        timestamp: Int
        tokentransferscount: Int
        type: String
        }

        """
        aggregated selection of "contract_factory_fa12_operations"
        """
        type contract_factory_fa12_operations_aggregate {
        aggregate: contract_factory_fa12_operations_aggregate_fields
        nodes: [contract_factory_fa12_operations!]!
        }

        """
        aggregate fields of "contract_factory_fa12_operations"
        """
        type contract_factory_fa12_operations_aggregate_fields {
        avg: contract_factory_fa12_operations_avg_fields
        count(columns: [contract_factory_fa12_operations_select_column!], distinct: Boolean): Int!
        max: contract_factory_fa12_operations_max_fields
        min: contract_factory_fa12_operations_min_fields
        stddev: contract_factory_fa12_operations_stddev_fields
        stddev_pop: contract_factory_fa12_operations_stddev_pop_fields
        stddev_samp: contract_factory_fa12_operations_stddev_samp_fields
        sum: contract_factory_fa12_operations_sum_fields
        var_pop: contract_factory_fa12_operations_var_pop_fields
        var_samp: contract_factory_fa12_operations_var_samp_fields
        variance: contract_factory_fa12_operations_variance_fields
        }

        """aggregate avg on columns"""
        type contract_factory_fa12_operations_avg_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """
        Boolean expression to filter rows from the table "contract_factory_fa12_operations". All fields are combined with a logical 'AND'.
        """
        input contract_factory_fa12_operations_bool_exp {
        _and: [contract_factory_fa12_operations_bool_exp!]
        _not: contract_factory_fa12_operations_bool_exp
        _or: [contract_factory_fa12_operations_bool_exp!]
        allocationfee: Int_comparison_exp
        amount: Int_comparison_exp
        bakerfee: Int_comparison_exp
        block: String_comparison_exp
        counter: Int_comparison_exp
        errors: String_comparison_exp
        eventscount: Int_comparison_exp
        gaslimit: Int_comparison_exp
        gasused: Int_comparison_exp
        hash: String_comparison_exp
        hasInternals: Boolean_comparison_exp
        id: Int_comparison_exp
        initiator: String_comparison_exp
        level: Int_comparison_exp
        nonce: Int_comparison_exp
        parameter: String_comparison_exp
        sender: String_comparison_exp
        sendercodehash: Int_comparison_exp
        status: String_comparison_exp
        storagefee: Int_comparison_exp
        storagelimit: Int_comparison_exp
        storageused: Int_comparison_exp
        target: String_comparison_exp
        targetcodehash: Int_comparison_exp
        timestamp: Int_comparison_exp
        tokentransferscount: Int_comparison_exp
        type: String_comparison_exp
        }

        """
        unique or primary key constraInts on table "contract_factory_fa12_operations"
        """
        enum contract_factory_fa12_operations_constraInt {
        """
        unique or primary key constraInt on columns "id"
        """
        contract_factory_fa12_operations_pkey
        }

        """
        input type for incrementing numeric columns in table "contract_factory_fa12_operations"
        """
        input contract_factory_fa12_operations_inc_input {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        counter: Int
        eventscount: Int
        gaslimit: Int
        gasused: Int
        id: Int
        level: Int
        nonce: Int
        sendercodehash: Int
        storagefee: Int
        storagelimit: Int
        storageused: Int
        targetcodehash: Int
        tokentransferscount: Int
        }

        """
        input type for inserting data Into table "contract_factory_fa12_operations"
        """
        input contract_factory_fa12_operations_insert_input {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        block: String
        counter: Int
        errors: String
        eventscount: Int
        gaslimit: Int
        gasused: Int
        hash: String
        hasInternals: Boolean
        id: Int
        initiator: String
        level: Int
        nonce: Int
        parameter: String
        sender: String
        sendercodehash: Int
        status: String
        storagefee: Int
        storagelimit: Int
        storageused: Int
        target: String
        targetcodehash: Int
        timestamp: Int
        tokentransferscount: Int
        type: String
        }

        """aggregate max on columns"""
        type contract_factory_fa12_operations_max_fields {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        block: String
        counter: Int
        errors: String
        eventscount: Int
        gaslimit: Int
        gasused: Int
        hash: String
        id: Int
        initiator: String
        level: Int
        nonce: Int
        parameter: String
        sender: String
        sendercodehash: Int
        status: String
        storagefee: Int
        storagelimit: Int
        storageused: Int
        target: String
        targetcodehash: Int
        timestamp: Int
        tokentransferscount: Int
        type: String
        }

        """aggregate min on columns"""
        type contract_factory_fa12_operations_min_fields {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        block: String
        counter: Int
        errors: String
        eventscount: Int
        gaslimit: Int
        gasused: Int
        hash: String
        id: Int
        initiator: String
        level: Int
        nonce: Int
        parameter: String
        sender: String
        sendercodehash: Int
        status: String
        storagefee: Int
        storagelimit: Int
        storageused: Int
        target: String
        targetcodehash: Int
        timestamp: Int
        tokentransferscount: Int
        type: String
        }

        """
        response of any mutation on the table "contract_factory_fa12_operations"
        """
        type contract_factory_fa12_operations_mutation_response {
        """number of rows affected by the mutation"""
        affected_rows: Int!

        """data from the rows affected by the mutation"""
        returning: [contract_factory_fa12_operations!]!
        }

        """
        on_conflict condition type for table "contract_factory_fa12_operations"
        """
        input contract_factory_fa12_operations_on_conflict {
        constraInt: contract_factory_fa12_operations_constraInt!
        update_columns: [contract_factory_fa12_operations_update_column!]! = []
        where: contract_factory_fa12_operations_bool_exp
        }

        """
        Ordering options when selecting data from "contract_factory_fa12_operations".
        """
        input contract_factory_fa12_operations_order_by {
        allocationfee: order_by
        amount: order_by
        bakerfee: order_by
        block: order_by
        counter: order_by
        errors: order_by
        eventscount: order_by
        gaslimit: order_by
        gasused: order_by
        hash: order_by
        hasInternals: order_by
        id: order_by
        initiator: order_by
        level: order_by
        nonce: order_by
        parameter: order_by
        sender: order_by
        sendercodehash: order_by
        status: order_by
        storagefee: order_by
        storagelimit: order_by
        storageused: order_by
        target: order_by
        targetcodehash: order_by
        timestamp: order_by
        tokentransferscount: order_by
        type: order_by
        }

        """primary key columns input for table: contract_factory_fa12_operations"""
        input contract_factory_fa12_operations_pk_columns_input {
        id: Int!
        }

        """
        select columns of table "contract_factory_fa12_operations"
        """
        enum contract_factory_fa12_operations_select_column {
        """column name"""
        allocationfee

        """column name"""
        amount

        """column name"""
        bakerfee

        """column name"""
        block

        """column name"""
        counter

        """column name"""
        errors

        """column name"""
        eventscount

        """column name"""
        gaslimit

        """column name"""
        gasused

        """column name"""
        hash

        """column name"""
        hasInternals

        """column name"""
        id

        """column name"""
        initiator

        """column name"""
        level

        """column name"""
        nonce

        """column name"""
        parameter

        """column name"""
        sender

        """column name"""
        sendercodehash

        """column name"""
        status

        """column name"""
        storagefee

        """column name"""
        storagelimit

        """column name"""
        storageused

        """column name"""
        target

        """column name"""
        targetcodehash

        """column name"""
        timestamp

        """column name"""
        tokentransferscount

        """column name"""
        type
        }

        """
        input type for updating data in table "contract_factory_fa12_operations"
        """
        input contract_factory_fa12_operations_set_input {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        block: String
        counter: Int
        errors: String
        eventscount: Int
        gaslimit: Int
        gasused: Int
        hash: String
        hasInternals: Boolean
        id: Int
        initiator: String
        level: Int
        nonce: Int
        parameter: String
        sender: String
        sendercodehash: Int
        status: String
        storagefee: Int
        storagelimit: Int
        storageused: Int
        target: String
        targetcodehash: Int
        timestamp: Int
        tokentransferscount: Int
        type: String
        }

        """aggregate stddev on columns"""
        type contract_factory_fa12_operations_stddev_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """aggregate stddev_pop on columns"""
        type contract_factory_fa12_operations_stddev_pop_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """aggregate stddev_samp on columns"""
        type contract_factory_fa12_operations_stddev_samp_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """
        Streaming cursor of the table "contract_factory_fa12_operations"
        """
        input contract_factory_fa12_operations_stream_cursor_input {
        """Stream column input with initial value"""
        initial_value: contract_factory_fa12_operations_stream_cursor_value_input!

        """cursor ordering"""
        ordering: cursor_ordering
        }

        """Initial value of the column from where the streaming should start"""
        input contract_factory_fa12_operations_stream_cursor_value_input {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        block: String
        counter: Int
        errors: String
        eventscount: Int
        gaslimit: Int
        gasused: Int
        hash: String
        hasInternals: Boolean
        id: Int
        initiator: String
        level: Int
        nonce: Int
        parameter: String
        sender: String
        sendercodehash: Int
        status: String
        storagefee: Int
        storagelimit: Int
        storageused: Int
        target: String
        targetcodehash: Int
        timestamp: Int
        tokentransferscount: Int
        type: String
        }

        """aggregate sum on columns"""
        type contract_factory_fa12_operations_sum_fields {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        counter: Int
        eventscount: Int
        gaslimit: Int
        gasused: Int
        id: Int
        level: Int
        nonce: Int
        sendercodehash: Int
        storagefee: Int
        storagelimit: Int
        storageused: Int
        targetcodehash: Int
        tokentransferscount: Int
        }

        """
        update columns of table "contract_factory_fa12_operations"
        """
        enum contract_factory_fa12_operations_update_column {
        """column name"""
        allocationfee

        """column name"""
        amount

        """column name"""
        bakerfee

        """column name"""
        block

        """column name"""
        counter

        """column name"""
        errors

        """column name"""
        eventscount

        """column name"""
        gaslimit

        """column name"""
        gasused

        """column name"""
        hash

        """column name"""
        hasInternals

        """column name"""
        id

        """column name"""
        initiator

        """column name"""
        level

        """column name"""
        nonce

        """column name"""
        parameter

        """column name"""
        sender

        """column name"""
        sendercodehash

        """column name"""
        status

        """column name"""
        storagefee

        """column name"""
        storagelimit

        """column name"""
        storageused

        """column name"""
        target

        """column name"""
        targetcodehash

        """column name"""
        timestamp

        """column name"""
        tokentransferscount

        """column name"""
        type
        }

        input contract_factory_fa12_operations_updates {
        """increments the numeric columns with given value of the filtered values"""
        _inc: contract_factory_fa12_operations_inc_input

        """sets the columns of the filtered rows to the given values"""
        _set: contract_factory_fa12_operations_set_input

        """filter the rows which have to be updated"""
        where: contract_factory_fa12_operations_bool_exp!
        }

        """aggregate var_pop on columns"""
        type contract_factory_fa12_operations_var_pop_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """aggregate var_samp on columns"""
        type contract_factory_fa12_operations_var_samp_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """aggregate variance on columns"""
        type contract_factory_fa12_operations_variance_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """
        columns and relationships of "contract_factory_fa12_storage"
        """
        type contract_factory_fa12_storage {
        counter: Int
        default_metadata: Int
        default_reserve: String
        default_token_metadata: Int
        empty_allowances: Int
        empty_history: Int
        empty_tokens: Int
        empty_user_investments: Int
        id: Int!
        swaps: Int
        token_to_swaps: Int
        }

        """
        aggregated selection of "contract_factory_fa12_storage"
        """
        type contract_factory_fa12_storage_aggregate {
        aggregate: contract_factory_fa12_storage_aggregate_fields
        nodes: [contract_factory_fa12_storage!]!
        }

        """
        aggregate fields of "contract_factory_fa12_storage"
        """
        type contract_factory_fa12_storage_aggregate_fields {
        avg: contract_factory_fa12_storage_avg_fields
        count(columns: [contract_factory_fa12_storage_select_column!], distinct: Boolean): Int!
        max: contract_factory_fa12_storage_max_fields
        min: contract_factory_fa12_storage_min_fields
        stddev: contract_factory_fa12_storage_stddev_fields
        stddev_pop: contract_factory_fa12_storage_stddev_pop_fields
        stddev_samp: contract_factory_fa12_storage_stddev_samp_fields
        sum: contract_factory_fa12_storage_sum_fields
        var_pop: contract_factory_fa12_storage_var_pop_fields
        var_samp: contract_factory_fa12_storage_var_samp_fields
        variance: contract_factory_fa12_storage_variance_fields
        }

        """aggregate avg on columns"""
        type contract_factory_fa12_storage_avg_fields {
        counter: Float
        default_metadata: Float
        default_token_metadata: Float
        empty_allowances: Float
        empty_history: Float
        empty_tokens: Float
        empty_user_investments: Float
        id: Float
        swaps: Float
        token_to_swaps: Float
        }

        """
        Boolean expression to filter rows from the table "contract_factory_fa12_storage". All fields are combined with a logical 'AND'.
        """
        input contract_factory_fa12_storage_bool_exp {
        _and: [contract_factory_fa12_storage_bool_exp!]
        _not: contract_factory_fa12_storage_bool_exp
        _or: [contract_factory_fa12_storage_bool_exp!]
        counter: Int_comparison_exp
        default_metadata: Int_comparison_exp
        default_reserve: String_comparison_exp
        default_token_metadata: Int_comparison_exp
        empty_allowances: Int_comparison_exp
        empty_history: Int_comparison_exp
        empty_tokens: Int_comparison_exp
        empty_user_investments: Int_comparison_exp
        id: Int_comparison_exp
        swaps: Int_comparison_exp
        token_to_swaps: Int_comparison_exp
        }

        """
        unique or primary key constraInts on table "contract_factory_fa12_storage"
        """
        enum contract_factory_fa12_storage_constraInt {
        """
        unique or primary key constraInt on columns "id"
        """
        contract_factory_fa12_storage_pkey
        }

        """
        input type for incrementing numeric columns in table "contract_factory_fa12_storage"
        """
        input contract_factory_fa12_storage_inc_input {
        counter: Int
        default_metadata: Int
        default_token_metadata: Int
        empty_allowances: Int
        empty_history: Int
        empty_tokens: Int
        empty_user_investments: Int
        id: Int
        swaps: Int
        token_to_swaps: Int
        }

        """
        input type for inserting data Into table "contract_factory_fa12_storage"
        """
        input contract_factory_fa12_storage_insert_input {
        counter: Int
        default_metadata: Int
        default_reserve: String
        default_token_metadata: Int
        empty_allowances: Int
        empty_history: Int
        empty_tokens: Int
        empty_user_investments: Int
        id: Int
        swaps: Int
        token_to_swaps: Int
        }

        """aggregate max on columns"""
        type contract_factory_fa12_storage_max_fields {
        counter: Int
        default_metadata: Int
        default_reserve: String
        default_token_metadata: Int
        empty_allowances: Int
        empty_history: Int
        empty_tokens: Int
        empty_user_investments: Int
        id: Int
        swaps: Int
        token_to_swaps: Int
        }

        """aggregate min on columns"""
        type contract_factory_fa12_storage_min_fields {
        counter: Int
        default_metadata: Int
        default_reserve: String
        default_token_metadata: Int
        empty_allowances: Int
        empty_history: Int
        empty_tokens: Int
        empty_user_investments: Int
        id: Int
        swaps: Int
        token_to_swaps: Int
        }

        """
        response of any mutation on the table "contract_factory_fa12_storage"
        """
        type contract_factory_fa12_storage_mutation_response {
        """number of rows affected by the mutation"""
        affected_rows: Int!

        """data from the rows affected by the mutation"""
        returning: [contract_factory_fa12_storage!]!
        }

        """
        on_conflict condition type for table "contract_factory_fa12_storage"
        """
        input contract_factory_fa12_storage_on_conflict {
        constraInt: contract_factory_fa12_storage_constraInt!
        update_columns: [contract_factory_fa12_storage_update_column!]! = []
        where: contract_factory_fa12_storage_bool_exp
        }

        """
        Ordering options when selecting data from "contract_factory_fa12_storage".
        """
        input contract_factory_fa12_storage_order_by {
        counter: order_by
        default_metadata: order_by
        default_reserve: order_by
        default_token_metadata: order_by
        empty_allowances: order_by
        empty_history: order_by
        empty_tokens: order_by
        empty_user_investments: order_by
        id: order_by
        swaps: order_by
        token_to_swaps: order_by
        }

        """primary key columns input for table: contract_factory_fa12_storage"""
        input contract_factory_fa12_storage_pk_columns_input {
        id: Int!
        }

        """
        select columns of table "contract_factory_fa12_storage"
        """
        enum contract_factory_fa12_storage_select_column {
        """column name"""
        counter

        """column name"""
        default_metadata

        """column name"""
        default_reserve

        """column name"""
        default_token_metadata

        """column name"""
        empty_allowances

        """column name"""
        empty_history

        """column name"""
        empty_tokens

        """column name"""
        empty_user_investments

        """column name"""
        id

        """column name"""
        swaps

        """column name"""
        token_to_swaps
        }

        """
        input type for updating data in table "contract_factory_fa12_storage"
        """
        input contract_factory_fa12_storage_set_input {
        counter: Int
        default_metadata: Int
        default_reserve: String
        default_token_metadata: Int
        empty_allowances: Int
        empty_history: Int
        empty_tokens: Int
        empty_user_investments: Int
        id: Int
        swaps: Int
        token_to_swaps: Int
        }

        """aggregate stddev on columns"""
        type contract_factory_fa12_storage_stddev_fields {
        counter: Float
        default_metadata: Float
        default_token_metadata: Float
        empty_allowances: Float
        empty_history: Float
        empty_tokens: Float
        empty_user_investments: Float
        id: Float
        swaps: Float
        token_to_swaps: Float
        }

        """aggregate stddev_pop on columns"""
        type contract_factory_fa12_storage_stddev_pop_fields {
        counter: Float
        default_metadata: Float
        default_token_metadata: Float
        empty_allowances: Float
        empty_history: Float
        empty_tokens: Float
        empty_user_investments: Float
        id: Float
        swaps: Float
        token_to_swaps: Float
        }

        """aggregate stddev_samp on columns"""
        type contract_factory_fa12_storage_stddev_samp_fields {
        counter: Float
        default_metadata: Float
        default_token_metadata: Float
        empty_allowances: Float
        empty_history: Float
        empty_tokens: Float
        empty_user_investments: Float
        id: Float
        swaps: Float
        token_to_swaps: Float
        }

        """
        Streaming cursor of the table "contract_factory_fa12_storage"
        """
        input contract_factory_fa12_storage_stream_cursor_input {
        """Stream column input with initial value"""
        initial_value: contract_factory_fa12_storage_stream_cursor_value_input!

        """cursor ordering"""
        ordering: cursor_ordering
        }

        """Initial value of the column from where the streaming should start"""
        input contract_factory_fa12_storage_stream_cursor_value_input {
        counter: Int
        default_metadata: Int
        default_reserve: String
        default_token_metadata: Int
        empty_allowances: Int
        empty_history: Int
        empty_tokens: Int
        empty_user_investments: Int
        id: Int
        swaps: Int
        token_to_swaps: Int
        }

        """aggregate sum on columns"""
        type contract_factory_fa12_storage_sum_fields {
        counter: Int
        default_metadata: Int
        default_token_metadata: Int
        empty_allowances: Int
        empty_history: Int
        empty_tokens: Int
        empty_user_investments: Int
        id: Int
        swaps: Int
        token_to_swaps: Int
        }

        """
        update columns of table "contract_factory_fa12_storage"
        """
        enum contract_factory_fa12_storage_update_column {
        """column name"""
        counter

        """column name"""
        default_metadata

        """column name"""
        default_reserve

        """column name"""
        default_token_metadata

        """column name"""
        empty_allowances

        """column name"""
        empty_history

        """column name"""
        empty_tokens

        """column name"""
        empty_user_investments

        """column name"""
        id

        """column name"""
        swaps

        """column name"""
        token_to_swaps
        }

        input contract_factory_fa12_storage_updates {
        """increments the numeric columns with given value of the filtered values"""
        _inc: contract_factory_fa12_storage_inc_input

        """sets the columns of the filtered rows to the given values"""
        _set: contract_factory_fa12_storage_set_input

        """filter the rows which have to be updated"""
        where: contract_factory_fa12_storage_bool_exp!
        }

        """aggregate var_pop on columns"""
        type contract_factory_fa12_storage_var_pop_fields {
        counter: Float
        default_metadata: Float
        default_token_metadata: Float
        empty_allowances: Float
        empty_history: Float
        empty_tokens: Float
        empty_user_investments: Float
        id: Float
        swaps: Float
        token_to_swaps: Float
        }

        """aggregate var_samp on columns"""
        type contract_factory_fa12_storage_var_samp_fields {
        counter: Float
        default_metadata: Float
        default_token_metadata: Float
        empty_allowances: Float
        empty_history: Float
        empty_tokens: Float
        empty_user_investments: Float
        id: Float
        swaps: Float
        token_to_swaps: Float
        }

        """aggregate variance on columns"""
        type contract_factory_fa12_storage_variance_fields {
        counter: Float
        default_metadata: Float
        default_token_metadata: Float
        empty_allowances: Float
        empty_history: Float
        empty_tokens: Float
        empty_user_investments: Float
        id: Float
        swaps: Float
        token_to_swaps: Float
        }

        """
        columns and relationships of "contract_factory_fa2_operations"
        """
        type contract_factory_fa2_operations {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        block: String
        counter: Int
        errors: String
        eventscount: Int
        gaslimit: Int
        gasused: Int
        hash: String
        hasInternals: Boolean
        id: Int!
        initiator: String
        level: Int
        nonce: Int
        parameter: String
        sender: String
        sendercodehash: Int
        status: String
        storagefee: Int
        storagelimit: Int
        storageused: Int
        target: String
        targetcodehash: Int
        timestamp: Int
        tokentransferscount: Int
        type: String
        }

        """
        aggregated selection of "contract_factory_fa2_operations"
        """
        type contract_factory_fa2_operations_aggregate {
        aggregate: contract_factory_fa2_operations_aggregate_fields
        nodes: [contract_factory_fa2_operations!]!
        }

        """
        aggregate fields of "contract_factory_fa2_operations"
        """
        type contract_factory_fa2_operations_aggregate_fields {
        avg: contract_factory_fa2_operations_avg_fields
        count(columns: [contract_factory_fa2_operations_select_column!], distinct: Boolean): Int!
        max: contract_factory_fa2_operations_max_fields
        min: contract_factory_fa2_operations_min_fields
        stddev: contract_factory_fa2_operations_stddev_fields
        stddev_pop: contract_factory_fa2_operations_stddev_pop_fields
        stddev_samp: contract_factory_fa2_operations_stddev_samp_fields
        sum: contract_factory_fa2_operations_sum_fields
        var_pop: contract_factory_fa2_operations_var_pop_fields
        var_samp: contract_factory_fa2_operations_var_samp_fields
        variance: contract_factory_fa2_operations_variance_fields
        }

        """aggregate avg on columns"""
        type contract_factory_fa2_operations_avg_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """
        Boolean expression to filter rows from the table "contract_factory_fa2_operations". All fields are combined with a logical 'AND'.
        """
        input contract_factory_fa2_operations_bool_exp {
        _and: [contract_factory_fa2_operations_bool_exp!]
        _not: contract_factory_fa2_operations_bool_exp
        _or: [contract_factory_fa2_operations_bool_exp!]
        allocationfee: Int_comparison_exp
        amount: Int_comparison_exp
        bakerfee: Int_comparison_exp
        block: String_comparison_exp
        counter: Int_comparison_exp
        errors: String_comparison_exp
        eventscount: Int_comparison_exp
        gaslimit: Int_comparison_exp
        gasused: Int_comparison_exp
        hash: String_comparison_exp
        hasInternals: Boolean_comparison_exp
        id: Int_comparison_exp
        initiator: String_comparison_exp
        level: Int_comparison_exp
        nonce: Int_comparison_exp
        parameter: String_comparison_exp
        sender: String_comparison_exp
        sendercodehash: Int_comparison_exp
        status: String_comparison_exp
        storagefee: Int_comparison_exp
        storagelimit: Int_comparison_exp
        storageused: Int_comparison_exp
        target: String_comparison_exp
        targetcodehash: Int_comparison_exp
        timestamp: Int_comparison_exp
        tokentransferscount: Int_comparison_exp
        type: String_comparison_exp
        }

        """
        unique or primary key constraInts on table "contract_factory_fa2_operations"
        """
        enum contract_factory_fa2_operations_constraInt {
        """
        unique or primary key constraInt on columns "id"
        """
        contract_factory_fa2_operations_pkey
        }

        """
        input type for incrementing numeric columns in table "contract_factory_fa2_operations"
        """
        input contract_factory_fa2_operations_inc_input {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        counter: Int
        eventscount: Int
        gaslimit: Int
        gasused: Int
        id: Int
        level: Int
        nonce: Int
        sendercodehash: Int
        storagefee: Int
        storagelimit: Int
        storageused: Int
        targetcodehash: Int
        tokentransferscount: Int
        }

        """
        input type for inserting data Into table "contract_factory_fa2_operations"
        """
        input contract_factory_fa2_operations_insert_input {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        block: String
        counter: Int
        errors: String
        eventscount: Int
        gaslimit: Int
        gasused: Int
        hash: String
        hasInternals: Boolean
        id: Int
        initiator: String
        level: Int
        nonce: Int
        parameter: String
        sender: String
        sendercodehash: Int
        status: String
        storagefee: Int
        storagelimit: Int
        storageused: Int
        target: String
        targetcodehash: Int
        timestamp: Int
        tokentransferscount: Int
        type: String
        }

        """aggregate max on columns"""
        type contract_factory_fa2_operations_max_fields {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        block: String
        counter: Int
        errors: String
        eventscount: Int
        gaslimit: Int
        gasused: Int
        hash: String
        id: Int
        initiator: String
        level: Int
        nonce: Int
        parameter: String
        sender: String
        sendercodehash: Int
        status: String
        storagefee: Int
        storagelimit: Int
        storageused: Int
        target: String
        targetcodehash: Int
        timestamp: Int
        tokentransferscount: Int
        type: String
        }

        """aggregate min on columns"""
        type contract_factory_fa2_operations_min_fields {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        block: String
        counter: Int
        errors: String
        eventscount: Int
        gaslimit: Int
        gasused: Int
        hash: String
        id: Int
        initiator: String
        level: Int
        nonce: Int
        parameter: String
        sender: String
        sendercodehash: Int
        status: String
        storagefee: Int
        storagelimit: Int
        storageused: Int
        target: String
        targetcodehash: Int
        timestamp: Int
        tokentransferscount: Int
        type: String
        }

        """
        response of any mutation on the table "contract_factory_fa2_operations"
        """
        type contract_factory_fa2_operations_mutation_response {
        """number of rows affected by the mutation"""
        affected_rows: Int!

        """data from the rows affected by the mutation"""
        returning: [contract_factory_fa2_operations!]!
        }

        """
        on_conflict condition type for table "contract_factory_fa2_operations"
        """
        input contract_factory_fa2_operations_on_conflict {
        constraInt: contract_factory_fa2_operations_constraInt!
        update_columns: [contract_factory_fa2_operations_update_column!]! = []
        where: contract_factory_fa2_operations_bool_exp
        }

        """
        Ordering options when selecting data from "contract_factory_fa2_operations".
        """
        input contract_factory_fa2_operations_order_by {
        allocationfee: order_by
        amount: order_by
        bakerfee: order_by
        block: order_by
        counter: order_by
        errors: order_by
        eventscount: order_by
        gaslimit: order_by
        gasused: order_by
        hash: order_by
        hasInternals: order_by
        id: order_by
        initiator: order_by
        level: order_by
        nonce: order_by
        parameter: order_by
        sender: order_by
        sendercodehash: order_by
        status: order_by
        storagefee: order_by
        storagelimit: order_by
        storageused: order_by
        target: order_by
        targetcodehash: order_by
        timestamp: order_by
        tokentransferscount: order_by
        type: order_by
        }

        """primary key columns input for table: contract_factory_fa2_operations"""
        input contract_factory_fa2_operations_pk_columns_input {
        id: Int!
        }

        """
        select columns of table "contract_factory_fa2_operations"
        """
        enum contract_factory_fa2_operations_select_column {
        """column name"""
        allocationfee

        """column name"""
        amount

        """column name"""
        bakerfee

        """column name"""
        block

        """column name"""
        counter

        """column name"""
        errors

        """column name"""
        eventscount

        """column name"""
        gaslimit

        """column name"""
        gasused

        """column name"""
        hash

        """column name"""
        hasInternals

        """column name"""
        id

        """column name"""
        initiator

        """column name"""
        level

        """column name"""
        nonce

        """column name"""
        parameter

        """column name"""
        sender

        """column name"""
        sendercodehash

        """column name"""
        status

        """column name"""
        storagefee

        """column name"""
        storagelimit

        """column name"""
        storageused

        """column name"""
        target

        """column name"""
        targetcodehash

        """column name"""
        timestamp

        """column name"""
        tokentransferscount

        """column name"""
        type
        }

        """
        input type for updating data in table "contract_factory_fa2_operations"
        """
        input contract_factory_fa2_operations_set_input {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        block: String
        counter: Int
        errors: String
        eventscount: Int
        gaslimit: Int
        gasused: Int
        hash: String
        hasInternals: Boolean
        id: Int
        initiator: String
        level: Int
        nonce: Int
        parameter: String
        sender: String
        sendercodehash: Int
        status: String
        storagefee: Int
        storagelimit: Int
        storageused: Int
        target: String
        targetcodehash: Int
        timestamp: Int
        tokentransferscount: Int
        type: String
        }

        """aggregate stddev on columns"""
        type contract_factory_fa2_operations_stddev_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """aggregate stddev_pop on columns"""
        type contract_factory_fa2_operations_stddev_pop_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """aggregate stddev_samp on columns"""
        type contract_factory_fa2_operations_stddev_samp_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """
        Streaming cursor of the table "contract_factory_fa2_operations"
        """
        input contract_factory_fa2_operations_stream_cursor_input {
        """Stream column input with initial value"""
        initial_value: contract_factory_fa2_operations_stream_cursor_value_input!

        """cursor ordering"""
        ordering: cursor_ordering
        }

        """Initial value of the column from where the streaming should start"""
        input contract_factory_fa2_operations_stream_cursor_value_input {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        block: String
        counter: Int
        errors: String
        eventscount: Int
        gaslimit: Int
        gasused: Int
        hash: String
        hasInternals: Boolean
        id: Int
        initiator: String
        level: Int
        nonce: Int
        parameter: String
        sender: String
        sendercodehash: Int
        status: String
        storagefee: Int
        storagelimit: Int
        storageused: Int
        target: String
        targetcodehash: Int
        timestamp: Int
        tokentransferscount: Int
        type: String
        }

        """aggregate sum on columns"""
        type contract_factory_fa2_operations_sum_fields {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        counter: Int
        eventscount: Int
        gaslimit: Int
        gasused: Int
        id: Int
        level: Int
        nonce: Int
        sendercodehash: Int
        storagefee: Int
        storagelimit: Int
        storageused: Int
        targetcodehash: Int
        tokentransferscount: Int
        }

        """
        update columns of table "contract_factory_fa2_operations"
        """
        enum contract_factory_fa2_operations_update_column {
        """column name"""
        allocationfee

        """column name"""
        amount

        """column name"""
        bakerfee

        """column name"""
        block

        """column name"""
        counter

        """column name"""
        errors

        """column name"""
        eventscount

        """column name"""
        gaslimit

        """column name"""
        gasused

        """column name"""
        hash

        """column name"""
        hasInternals

        """column name"""
        id

        """column name"""
        initiator

        """column name"""
        level

        """column name"""
        nonce

        """column name"""
        parameter

        """column name"""
        sender

        """column name"""
        sendercodehash

        """column name"""
        status

        """column name"""
        storagefee

        """column name"""
        storagelimit

        """column name"""
        storageused

        """column name"""
        target

        """column name"""
        targetcodehash

        """column name"""
        timestamp

        """column name"""
        tokentransferscount

        """column name"""
        type
        }

        input contract_factory_fa2_operations_updates {
        """increments the numeric columns with given value of the filtered values"""
        _inc: contract_factory_fa2_operations_inc_input

        """sets the columns of the filtered rows to the given values"""
        _set: contract_factory_fa2_operations_set_input

        """filter the rows which have to be updated"""
        where: contract_factory_fa2_operations_bool_exp!
        }

        """aggregate var_pop on columns"""
        type contract_factory_fa2_operations_var_pop_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """aggregate var_samp on columns"""
        type contract_factory_fa2_operations_var_samp_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """aggregate variance on columns"""
        type contract_factory_fa2_operations_variance_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """
        columns and relationships of "contract_factory_fa2_storage"
        """
        type contract_factory_fa2_storage {
        counter: Int
        default_metadata: Int
        default_reserve: String
        default_token_metadata: Int
        empty_allowances: Int
        empty_history: Int
        empty_tokens: Int
        empty_user_investments: Int
        id: Int!
        swaps: Int
        token_to_swaps: Int
        }

        """
        aggregated selection of "contract_factory_fa2_storage"
        """
        type contract_factory_fa2_storage_aggregate {
        aggregate: contract_factory_fa2_storage_aggregate_fields
        nodes: [contract_factory_fa2_storage!]!
        }

        """
        aggregate fields of "contract_factory_fa2_storage"
        """
        type contract_factory_fa2_storage_aggregate_fields {
        avg: contract_factory_fa2_storage_avg_fields
        count(columns: [contract_factory_fa2_storage_select_column!], distinct: Boolean): Int!
        max: contract_factory_fa2_storage_max_fields
        min: contract_factory_fa2_storage_min_fields
        stddev: contract_factory_fa2_storage_stddev_fields
        stddev_pop: contract_factory_fa2_storage_stddev_pop_fields
        stddev_samp: contract_factory_fa2_storage_stddev_samp_fields
        sum: contract_factory_fa2_storage_sum_fields
        var_pop: contract_factory_fa2_storage_var_pop_fields
        var_samp: contract_factory_fa2_storage_var_samp_fields
        variance: contract_factory_fa2_storage_variance_fields
        }

        """aggregate avg on columns"""
        type contract_factory_fa2_storage_avg_fields {
        counter: Float
        default_metadata: Float
        default_token_metadata: Float
        empty_allowances: Float
        empty_history: Float
        empty_tokens: Float
        empty_user_investments: Float
        id: Float
        swaps: Float
        token_to_swaps: Float
        }

        """
        Boolean expression to filter rows from the table "contract_factory_fa2_storage". All fields are combined with a logical 'AND'.
        """
        input contract_factory_fa2_storage_bool_exp {
        _and: [contract_factory_fa2_storage_bool_exp!]
        _not: contract_factory_fa2_storage_bool_exp
        _or: [contract_factory_fa2_storage_bool_exp!]
        counter: Int_comparison_exp
        default_metadata: Int_comparison_exp
        default_reserve: String_comparison_exp
        default_token_metadata: Int_comparison_exp
        empty_allowances: Int_comparison_exp
        empty_history: Int_comparison_exp
        empty_tokens: Int_comparison_exp
        empty_user_investments: Int_comparison_exp
        id: Int_comparison_exp
        swaps: Int_comparison_exp
        token_to_swaps: Int_comparison_exp
        }

        """
        unique or primary key constraInts on table "contract_factory_fa2_storage"
        """
        enum contract_factory_fa2_storage_constraInt {
        """
        unique or primary key constraInt on columns "id"
        """
        contract_factory_fa2_storage_pkey
        }

        """
        input type for incrementing numeric columns in table "contract_factory_fa2_storage"
        """
        input contract_factory_fa2_storage_inc_input {
        counter: Int
        default_metadata: Int
        default_token_metadata: Int
        empty_allowances: Int
        empty_history: Int
        empty_tokens: Int
        empty_user_investments: Int
        id: Int
        swaps: Int
        token_to_swaps: Int
        }

        """
        input type for inserting data Into table "contract_factory_fa2_storage"
        """
        input contract_factory_fa2_storage_insert_input {
        counter: Int
        default_metadata: Int
        default_reserve: String
        default_token_metadata: Int
        empty_allowances: Int
        empty_history: Int
        empty_tokens: Int
        empty_user_investments: Int
        id: Int
        swaps: Int
        token_to_swaps: Int
        }

        """aggregate max on columns"""
        type contract_factory_fa2_storage_max_fields {
        counter: Int
        default_metadata: Int
        default_reserve: String
        default_token_metadata: Int
        empty_allowances: Int
        empty_history: Int
        empty_tokens: Int
        empty_user_investments: Int
        id: Int
        swaps: Int
        token_to_swaps: Int
        }

        """aggregate min on columns"""
        type contract_factory_fa2_storage_min_fields {
        counter: Int
        default_metadata: Int
        default_reserve: String
        default_token_metadata: Int
        empty_allowances: Int
        empty_history: Int
        empty_tokens: Int
        empty_user_investments: Int
        id: Int
        swaps: Int
        token_to_swaps: Int
        }

        """
        response of any mutation on the table "contract_factory_fa2_storage"
        """
        type contract_factory_fa2_storage_mutation_response {
        """number of rows affected by the mutation"""
        affected_rows: Int!

        """data from the rows affected by the mutation"""
        returning: [contract_factory_fa2_storage!]!
        }

        """
        on_conflict condition type for table "contract_factory_fa2_storage"
        """
        input contract_factory_fa2_storage_on_conflict {
        constraInt: contract_factory_fa2_storage_constraInt!
        update_columns: [contract_factory_fa2_storage_update_column!]! = []
        where: contract_factory_fa2_storage_bool_exp
        }

        """
        Ordering options when selecting data from "contract_factory_fa2_storage".
        """
        input contract_factory_fa2_storage_order_by {
        counter: order_by
        default_metadata: order_by
        default_reserve: order_by
        default_token_metadata: order_by
        empty_allowances: order_by
        empty_history: order_by
        empty_tokens: order_by
        empty_user_investments: order_by
        id: order_by
        swaps: order_by
        token_to_swaps: order_by
        }

        """primary key columns input for table: contract_factory_fa2_storage"""
        input contract_factory_fa2_storage_pk_columns_input {
        id: Int!
        }

        """
        select columns of table "contract_factory_fa2_storage"
        """
        enum contract_factory_fa2_storage_select_column {
        """column name"""
        counter

        """column name"""
        default_metadata

        """column name"""
        default_reserve

        """column name"""
        default_token_metadata

        """column name"""
        empty_allowances

        """column name"""
        empty_history

        """column name"""
        empty_tokens

        """column name"""
        empty_user_investments

        """column name"""
        id

        """column name"""
        swaps

        """column name"""
        token_to_swaps
        }

        """
        input type for updating data in table "contract_factory_fa2_storage"
        """
        input contract_factory_fa2_storage_set_input {
        counter: Int
        default_metadata: Int
        default_reserve: String
        default_token_metadata: Int
        empty_allowances: Int
        empty_history: Int
        empty_tokens: Int
        empty_user_investments: Int
        id: Int
        swaps: Int
        token_to_swaps: Int
        }

        """aggregate stddev on columns"""
        type contract_factory_fa2_storage_stddev_fields {
        counter: Float
        default_metadata: Float
        default_token_metadata: Float
        empty_allowances: Float
        empty_history: Float
        empty_tokens: Float
        empty_user_investments: Float
        id: Float
        swaps: Float
        token_to_swaps: Float
        }

        """aggregate stddev_pop on columns"""
        type contract_factory_fa2_storage_stddev_pop_fields {
        counter: Float
        default_metadata: Float
        default_token_metadata: Float
        empty_allowances: Float
        empty_history: Float
        empty_tokens: Float
        empty_user_investments: Float
        id: Float
        swaps: Float
        token_to_swaps: Float
        }

        """aggregate stddev_samp on columns"""
        type contract_factory_fa2_storage_stddev_samp_fields {
        counter: Float
        default_metadata: Float
        default_token_metadata: Float
        empty_allowances: Float
        empty_history: Float
        empty_tokens: Float
        empty_user_investments: Float
        id: Float
        swaps: Float
        token_to_swaps: Float
        }

        """
        Streaming cursor of the table "contract_factory_fa2_storage"
        """
        input contract_factory_fa2_storage_stream_cursor_input {
        """Stream column input with initial value"""
        initial_value: contract_factory_fa2_storage_stream_cursor_value_input!

        """cursor ordering"""
        ordering: cursor_ordering
        }

        """Initial value of the column from where the streaming should start"""
        input contract_factory_fa2_storage_stream_cursor_value_input {
        counter: Int
        default_metadata: Int
        default_reserve: String
        default_token_metadata: Int
        empty_allowances: Int
        empty_history: Int
        empty_tokens: Int
        empty_user_investments: Int
        id: Int
        swaps: Int
        token_to_swaps: Int
        }

        """aggregate sum on columns"""
        type contract_factory_fa2_storage_sum_fields {
        counter: Int
        default_metadata: Int
        default_token_metadata: Int
        empty_allowances: Int
        empty_history: Int
        empty_tokens: Int
        empty_user_investments: Int
        id: Int
        swaps: Int
        token_to_swaps: Int
        }

        """
        update columns of table "contract_factory_fa2_storage"
        """
        enum contract_factory_fa2_storage_update_column {
        """column name"""
        counter

        """column name"""
        default_metadata

        """column name"""
        default_reserve

        """column name"""
        default_token_metadata

        """column name"""
        empty_allowances

        """column name"""
        empty_history

        """column name"""
        empty_tokens

        """column name"""
        empty_user_investments

        """column name"""
        id

        """column name"""
        swaps

        """column name"""
        token_to_swaps
        }

        input contract_factory_fa2_storage_updates {
        """increments the numeric columns with given value of the filtered values"""
        _inc: contract_factory_fa2_storage_inc_input

        """sets the columns of the filtered rows to the given values"""
        _set: contract_factory_fa2_storage_set_input

        """filter the rows which have to be updated"""
        where: contract_factory_fa2_storage_bool_exp!
        }

        """aggregate var_pop on columns"""
        type contract_factory_fa2_storage_var_pop_fields {
        counter: Float
        default_metadata: Float
        default_token_metadata: Float
        empty_allowances: Float
        empty_history: Float
        empty_tokens: Float
        empty_user_investments: Float
        id: Float
        swaps: Float
        token_to_swaps: Float
        }

        """aggregate var_samp on columns"""
        type contract_factory_fa2_storage_var_samp_fields {
        counter: Float
        default_metadata: Float
        default_token_metadata: Float
        empty_allowances: Float
        empty_history: Float
        empty_tokens: Float
        empty_user_investments: Float
        id: Float
        swaps: Float
        token_to_swaps: Float
        }

        """aggregate variance on columns"""
        type contract_factory_fa2_storage_variance_fields {
        counter: Float
        default_metadata: Float
        default_token_metadata: Float
        empty_allowances: Float
        empty_history: Float
        empty_tokens: Float
        empty_user_investments: Float
        id: Float
        swaps: Float
        token_to_swaps: Float
        }

        """
        columns and relationships of "contract_farms_v1_operations"
        """
        type contract_farms_v1_operations {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        block: String
        counter: Int
        errors: String
        eventscount: Int
        gaslimit: Int
        gasused: Int
        hash: String
        hasInternals: Boolean
        id: Int!
        initiator: String
        level: Int
        nonce: Int
        parameter: String
        sender: String
        sendercodehash: Int
        status: String
        storagefee: Int
        storagelimit: Int
        storageused: Int
        target: String
        targetcodehash: Int
        timestamp: Int
        tokentransferscount: Int
        type: String
        }

        """
        aggregated selection of "contract_farms_v1_operations"
        """
        type contract_farms_v1_operations_aggregate {
        aggregate: contract_farms_v1_operations_aggregate_fields
        nodes: [contract_farms_v1_operations!]!
        }

        """
        aggregate fields of "contract_farms_v1_operations"
        """
        type contract_farms_v1_operations_aggregate_fields {
        avg: contract_farms_v1_operations_avg_fields
        count(columns: [contract_farms_v1_operations_select_column!], distinct: Boolean): Int!
        max: contract_farms_v1_operations_max_fields
        min: contract_farms_v1_operations_min_fields
        stddev: contract_farms_v1_operations_stddev_fields
        stddev_pop: contract_farms_v1_operations_stddev_pop_fields
        stddev_samp: contract_farms_v1_operations_stddev_samp_fields
        sum: contract_farms_v1_operations_sum_fields
        var_pop: contract_farms_v1_operations_var_pop_fields
        var_samp: contract_farms_v1_operations_var_samp_fields
        variance: contract_farms_v1_operations_variance_fields
        }

        """aggregate avg on columns"""
        type contract_farms_v1_operations_avg_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """
        Boolean expression to filter rows from the table "contract_farms_v1_operations". All fields are combined with a logical 'AND'.
        """
        input contract_farms_v1_operations_bool_exp {
        _and: [contract_farms_v1_operations_bool_exp!]
        _not: contract_farms_v1_operations_bool_exp
        _or: [contract_farms_v1_operations_bool_exp!]
        allocationfee: Int_comparison_exp
        amount: Int_comparison_exp
        bakerfee: Int_comparison_exp
        block: String_comparison_exp
        counter: Int_comparison_exp
        errors: String_comparison_exp
        eventscount: Int_comparison_exp
        gaslimit: Int_comparison_exp
        gasused: Int_comparison_exp
        hash: String_comparison_exp
        hasInternals: Boolean_comparison_exp
        id: Int_comparison_exp
        initiator: String_comparison_exp
        level: Int_comparison_exp
        nonce: Int_comparison_exp
        parameter: String_comparison_exp
        sender: String_comparison_exp
        sendercodehash: Int_comparison_exp
        status: String_comparison_exp
        storagefee: Int_comparison_exp
        storagelimit: Int_comparison_exp
        storageused: Int_comparison_exp
        target: String_comparison_exp
        targetcodehash: Int_comparison_exp
        timestamp: Int_comparison_exp
        tokentransferscount: Int_comparison_exp
        type: String_comparison_exp
        }

        """
        unique or primary key constraInts on table "contract_farms_v1_operations"
        """
        enum contract_farms_v1_operations_constraInt {
        """
        unique or primary key constraInt on columns "id"
        """
        contract_farms_v1_pkey
        }

        """
        input type for incrementing numeric columns in table "contract_farms_v1_operations"
        """
        input contract_farms_v1_operations_inc_input {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        counter: Int
        eventscount: Int
        gaslimit: Int
        gasused: Int
        id: Int
        level: Int
        nonce: Int
        sendercodehash: Int
        storagefee: Int
        storagelimit: Int
        storageused: Int
        targetcodehash: Int
        tokentransferscount: Int
        }

        """
        input type for inserting data Into table "contract_farms_v1_operations"
        """
        input contract_farms_v1_operations_insert_input {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        block: String
        counter: Int
        errors: String
        eventscount: Int
        gaslimit: Int
        gasused: Int
        hash: String
        hasInternals: Boolean
        id: Int
        initiator: String
        level: Int
        nonce: Int
        parameter: String
        sender: String
        sendercodehash: Int
        status: String
        storagefee: Int
        storagelimit: Int
        storageused: Int
        target: String
        targetcodehash: Int
        timestamp: Int
        tokentransferscount: Int
        type: String
        }

        """aggregate max on columns"""
        type contract_farms_v1_operations_max_fields {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        block: String
        counter: Int
        errors: String
        eventscount: Int
        gaslimit: Int
        gasused: Int
        hash: String
        id: Int
        initiator: String
        level: Int
        nonce: Int
        parameter: String
        sender: String
        sendercodehash: Int
        status: String
        storagefee: Int
        storagelimit: Int
        storageused: Int
        target: String
        targetcodehash: Int
        timestamp: Int
        tokentransferscount: Int
        type: String
        }

        """aggregate min on columns"""
        type contract_farms_v1_operations_min_fields {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        block: String
        counter: Int
        errors: String
        eventscount: Int
        gaslimit: Int
        gasused: Int
        hash: String
        id: Int
        initiator: String
        level: Int
        nonce: Int
        parameter: String
        sender: String
        sendercodehash: Int
        status: String
        storagefee: Int
        storagelimit: Int
        storageused: Int
        target: String
        targetcodehash: Int
        timestamp: Int
        tokentransferscount: Int
        type: String
        }

        """
        response of any mutation on the table "contract_farms_v1_operations"
        """
        type contract_farms_v1_operations_mutation_response {
        """number of rows affected by the mutation"""
        affected_rows: Int!

        """data from the rows affected by the mutation"""
        returning: [contract_farms_v1_operations!]!
        }

        """
        on_conflict condition type for table "contract_farms_v1_operations"
        """
        input contract_farms_v1_operations_on_conflict {
        constraInt: contract_farms_v1_operations_constraInt!
        update_columns: [contract_farms_v1_operations_update_column!]! = []
        where: contract_farms_v1_operations_bool_exp
        }

        """
        Ordering options when selecting data from "contract_farms_v1_operations".
        """
        input contract_farms_v1_operations_order_by {
        allocationfee: order_by
        amount: order_by
        bakerfee: order_by
        block: order_by
        counter: order_by
        errors: order_by
        eventscount: order_by
        gaslimit: order_by
        gasused: order_by
        hash: order_by
        hasInternals: order_by
        id: order_by
        initiator: order_by
        level: order_by
        nonce: order_by
        parameter: order_by
        sender: order_by
        sendercodehash: order_by
        status: order_by
        storagefee: order_by
        storagelimit: order_by
        storageused: order_by
        target: order_by
        targetcodehash: order_by
        timestamp: order_by
        tokentransferscount: order_by
        type: order_by
        }

        """primary key columns input for table: contract_farms_v1_operations"""
        input contract_farms_v1_operations_pk_columns_input {
        id: Int!
        }

        """
        select columns of table "contract_farms_v1_operations"
        """
        enum contract_farms_v1_operations_select_column {
        """column name"""
        allocationfee

        """column name"""
        amount

        """column name"""
        bakerfee

        """column name"""
        block

        """column name"""
        counter

        """column name"""
        errors

        """column name"""
        eventscount

        """column name"""
        gaslimit

        """column name"""
        gasused

        """column name"""
        hash

        """column name"""
        hasInternals

        """column name"""
        id

        """column name"""
        initiator

        """column name"""
        level

        """column name"""
        nonce

        """column name"""
        parameter

        """column name"""
        sender

        """column name"""
        sendercodehash

        """column name"""
        status

        """column name"""
        storagefee

        """column name"""
        storagelimit

        """column name"""
        storageused

        """column name"""
        target

        """column name"""
        targetcodehash

        """column name"""
        timestamp

        """column name"""
        tokentransferscount

        """column name"""
        type
        }

        """
        input type for updating data in table "contract_farms_v1_operations"
        """
        input contract_farms_v1_operations_set_input {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        block: String
        counter: Int
        errors: String
        eventscount: Int
        gaslimit: Int
        gasused: Int
        hash: String
        hasInternals: Boolean
        id: Int
        initiator: String
        level: Int
        nonce: Int
        parameter: String
        sender: String
        sendercodehash: Int
        status: String
        storagefee: Int
        storagelimit: Int
        storageused: Int
        target: String
        targetcodehash: Int
        timestamp: Int
        tokentransferscount: Int
        type: String
        }

        """aggregate stddev on columns"""
        type contract_farms_v1_operations_stddev_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """aggregate stddev_pop on columns"""
        type contract_farms_v1_operations_stddev_pop_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """aggregate stddev_samp on columns"""
        type contract_farms_v1_operations_stddev_samp_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """
        Streaming cursor of the table "contract_farms_v1_operations"
        """
        input contract_farms_v1_operations_stream_cursor_input {
        """Stream column input with initial value"""
        initial_value: contract_farms_v1_operations_stream_cursor_value_input!

        """cursor ordering"""
        ordering: cursor_ordering
        }

        """Initial value of the column from where the streaming should start"""
        input contract_farms_v1_operations_stream_cursor_value_input {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        block: String
        counter: Int
        errors: String
        eventscount: Int
        gaslimit: Int
        gasused: Int
        hash: String
        hasInternals: Boolean
        id: Int
        initiator: String
        level: Int
        nonce: Int
        parameter: String
        sender: String
        sendercodehash: Int
        status: String
        storagefee: Int
        storagelimit: Int
        storageused: Int
        target: String
        targetcodehash: Int
        timestamp: Int
        tokentransferscount: Int
        type: String
        }

        """aggregate sum on columns"""
        type contract_farms_v1_operations_sum_fields {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        counter: Int
        eventscount: Int
        gaslimit: Int
        gasused: Int
        id: Int
        level: Int
        nonce: Int
        sendercodehash: Int
        storagefee: Int
        storagelimit: Int
        storageused: Int
        targetcodehash: Int
        tokentransferscount: Int
        }

        """
        update columns of table "contract_farms_v1_operations"
        """
        enum contract_farms_v1_operations_update_column {
        """column name"""
        allocationfee

        """column name"""
        amount

        """column name"""
        bakerfee

        """column name"""
        block

        """column name"""
        counter

        """column name"""
        errors

        """column name"""
        eventscount

        """column name"""
        gaslimit

        """column name"""
        gasused

        """column name"""
        hash

        """column name"""
        hasInternals

        """column name"""
        id

        """column name"""
        initiator

        """column name"""
        level

        """column name"""
        nonce

        """column name"""
        parameter

        """column name"""
        sender

        """column name"""
        sendercodehash

        """column name"""
        status

        """column name"""
        storagefee

        """column name"""
        storagelimit

        """column name"""
        storageused

        """column name"""
        target

        """column name"""
        targetcodehash

        """column name"""
        timestamp

        """column name"""
        tokentransferscount

        """column name"""
        type
        }

        input contract_farms_v1_operations_updates {
        """increments the numeric columns with given value of the filtered values"""
        _inc: contract_farms_v1_operations_inc_input

        """sets the columns of the filtered rows to the given values"""
        _set: contract_farms_v1_operations_set_input

        """filter the rows which have to be updated"""
        where: contract_farms_v1_operations_bool_exp!
        }

        """aggregate var_pop on columns"""
        type contract_farms_v1_operations_var_pop_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """aggregate var_samp on columns"""
        type contract_farms_v1_operations_var_samp_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """aggregate variance on columns"""
        type contract_farms_v1_operations_variance_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """
        columns and relationships of "contract_farms_v1_storage"
        """
        type contract_farms_v1_storage {
        admin: String
        all_farms_data: Int
        id: Int!
        inverse_farms: Int
        }

        """
        aggregated selection of "contract_farms_v1_storage"
        """
        type contract_farms_v1_storage_aggregate {
        aggregate: contract_farms_v1_storage_aggregate_fields
        nodes: [contract_farms_v1_storage!]!
        }

        """
        aggregate fields of "contract_farms_v1_storage"
        """
        type contract_farms_v1_storage_aggregate_fields {
        avg: contract_farms_v1_storage_avg_fields
        count(columns: [contract_farms_v1_storage_select_column!], distinct: Boolean): Int!
        max: contract_farms_v1_storage_max_fields
        min: contract_farms_v1_storage_min_fields
        stddev: contract_farms_v1_storage_stddev_fields
        stddev_pop: contract_farms_v1_storage_stddev_pop_fields
        stddev_samp: contract_farms_v1_storage_stddev_samp_fields
        sum: contract_farms_v1_storage_sum_fields
        var_pop: contract_farms_v1_storage_var_pop_fields
        var_samp: contract_farms_v1_storage_var_samp_fields
        variance: contract_farms_v1_storage_variance_fields
        }

        """aggregate avg on columns"""
        type contract_farms_v1_storage_avg_fields {
        all_farms_data: Float
        id: Float
        inverse_farms: Float
        }

        """
        Boolean expression to filter rows from the table "contract_farms_v1_storage". All fields are combined with a logical 'AND'.
        """
        input contract_farms_v1_storage_bool_exp {
        _and: [contract_farms_v1_storage_bool_exp!]
        _not: contract_farms_v1_storage_bool_exp
        _or: [contract_farms_v1_storage_bool_exp!]
        admin: String_comparison_exp
        all_farms_data: Int_comparison_exp
        id: Int_comparison_exp
        inverse_farms: Int_comparison_exp
        }

        """
        unique or primary key constraInts on table "contract_farms_v1_storage"
        """
        enum contract_farms_v1_storage_constraInt {
        """
        unique or primary key constraInt on columns "id"
        """
        contract_farms_v1_storage_pkey
        }

        """
        input type for incrementing numeric columns in table "contract_farms_v1_storage"
        """
        input contract_farms_v1_storage_inc_input {
        all_farms_data: Int
        id: Int
        inverse_farms: Int
        }

        """
        input type for inserting data Into table "contract_farms_v1_storage"
        """
        input contract_farms_v1_storage_insert_input {
        admin: String
        all_farms_data: Int
        id: Int
        inverse_farms: Int
        }

        """aggregate max on columns"""
        type contract_farms_v1_storage_max_fields {
        admin: String
        all_farms_data: Int
        id: Int
        inverse_farms: Int
        }

        """aggregate min on columns"""
        type contract_farms_v1_storage_min_fields {
        admin: String
        all_farms_data: Int
        id: Int
        inverse_farms: Int
        }

        """
        response of any mutation on the table "contract_farms_v1_storage"
        """
        type contract_farms_v1_storage_mutation_response {
        """number of rows affected by the mutation"""
        affected_rows: Int!

        """data from the rows affected by the mutation"""
        returning: [contract_farms_v1_storage!]!
        }

        """
        on_conflict condition type for table "contract_farms_v1_storage"
        """
        input contract_farms_v1_storage_on_conflict {
        constraInt: contract_farms_v1_storage_constraInt!
        update_columns: [contract_farms_v1_storage_update_column!]! = []
        where: contract_farms_v1_storage_bool_exp
        }

        """Ordering options when selecting data from "contract_farms_v1_storage"."""
        input contract_farms_v1_storage_order_by {
        admin: order_by
        all_farms_data: order_by
        id: order_by
        inverse_farms: order_by
        }

        """primary key columns input for table: contract_farms_v1_storage"""
        input contract_farms_v1_storage_pk_columns_input {
        id: Int!
        }

        """
        select columns of table "contract_farms_v1_storage"
        """
        enum contract_farms_v1_storage_select_column {
        """column name"""
        admin

        """column name"""
        all_farms_data

        """column name"""
        id

        """column name"""
        inverse_farms
        }

        """
        input type for updating data in table "contract_farms_v1_storage"
        """
        input contract_farms_v1_storage_set_input {
        admin: String
        all_farms_data: Int
        id: Int
        inverse_farms: Int
        }

        """aggregate stddev on columns"""
        type contract_farms_v1_storage_stddev_fields {
        all_farms_data: Float
        id: Float
        inverse_farms: Float
        }

        """aggregate stddev_pop on columns"""
        type contract_farms_v1_storage_stddev_pop_fields {
        all_farms_data: Float
        id: Float
        inverse_farms: Float
        }

        """aggregate stddev_samp on columns"""
        type contract_farms_v1_storage_stddev_samp_fields {
        all_farms_data: Float
        id: Float
        inverse_farms: Float
        }

        """
        Streaming cursor of the table "contract_farms_v1_storage"
        """
        input contract_farms_v1_storage_stream_cursor_input {
        """Stream column input with initial value"""
        initial_value: contract_farms_v1_storage_stream_cursor_value_input!

        """cursor ordering"""
        ordering: cursor_ordering
        }

        """Initial value of the column from where the streaming should start"""
        input contract_farms_v1_storage_stream_cursor_value_input {
        admin: String
        all_farms_data: Int
        id: Int
        inverse_farms: Int
        }

        """aggregate sum on columns"""
        type contract_farms_v1_storage_sum_fields {
        all_farms_data: Int
        id: Int
        inverse_farms: Int
        }

        """
        update columns of table "contract_farms_v1_storage"
        """
        enum contract_farms_v1_storage_update_column {
        """column name"""
        admin

        """column name"""
        all_farms_data

        """column name"""
        id

        """column name"""
        inverse_farms
        }

        input contract_farms_v1_storage_updates {
        """increments the numeric columns with given value of the filtered values"""
        _inc: contract_farms_v1_storage_inc_input

        """sets the columns of the filtered rows to the given values"""
        _set: contract_farms_v1_storage_set_input

        """filter the rows which have to be updated"""
        where: contract_farms_v1_storage_bool_exp!
        }

        """aggregate var_pop on columns"""
        type contract_farms_v1_storage_var_pop_fields {
        all_farms_data: Float
        id: Float
        inverse_farms: Float
        }

        """aggregate var_samp on columns"""
        type contract_farms_v1_storage_var_samp_fields {
        all_farms_data: Float
        id: Float
        inverse_farms: Float
        }

        """aggregate variance on columns"""
        type contract_farms_v1_storage_variance_fields {
        all_farms_data: Float
        id: Float
        inverse_farms: Float
        }

        """
        columns and relationships of "contract_farms_v2_allfarms"
        """
        type contract_farms_v2_allfarms {
        address: String
        factory: Int
        id: Int!
        }

        """
        aggregated selection of "contract_farms_v2_allfarms"
        """
        type contract_farms_v2_allfarms_aggregate {
        aggregate: contract_farms_v2_allfarms_aggregate_fields
        nodes: [contract_farms_v2_allfarms!]!
        }

        """
        aggregate fields of "contract_farms_v2_allfarms"
        """
        type contract_farms_v2_allfarms_aggregate_fields {
        avg: contract_farms_v2_allfarms_avg_fields
        count(columns: [contract_farms_v2_allfarms_select_column!], distinct: Boolean): Int!
        max: contract_farms_v2_allfarms_max_fields
        min: contract_farms_v2_allfarms_min_fields
        stddev: contract_farms_v2_allfarms_stddev_fields
        stddev_pop: contract_farms_v2_allfarms_stddev_pop_fields
        stddev_samp: contract_farms_v2_allfarms_stddev_samp_fields
        sum: contract_farms_v2_allfarms_sum_fields
        var_pop: contract_farms_v2_allfarms_var_pop_fields
        var_samp: contract_farms_v2_allfarms_var_samp_fields
        variance: contract_farms_v2_allfarms_variance_fields
        }

        """aggregate avg on columns"""
        type contract_farms_v2_allfarms_avg_fields {
        factory: Float
        id: Float
        }

        """
        Boolean expression to filter rows from the table "contract_farms_v2_allfarms". All fields are combined with a logical 'AND'.
        """
        input contract_farms_v2_allfarms_bool_exp {
        _and: [contract_farms_v2_allfarms_bool_exp!]
        _not: contract_farms_v2_allfarms_bool_exp
        _or: [contract_farms_v2_allfarms_bool_exp!]
        address: String_comparison_exp
        factory: Int_comparison_exp
        id: Int_comparison_exp
        }

        """
        unique or primary key constraInts on table "contract_farms_v2_allfarms"
        """
        enum contract_farms_v2_allfarms_constraInt {
        """
        unique or primary key constraInt on columns "id"
        """
        contract_farms_v2_allfarms_pkey
        }

        """
        input type for incrementing numeric columns in table "contract_farms_v2_allfarms"
        """
        input contract_farms_v2_allfarms_inc_input {
        factory: Int
        id: Int
        }

        """
        input type for inserting data Into table "contract_farms_v2_allfarms"
        """
        input contract_farms_v2_allfarms_insert_input {
        address: String
        factory: Int
        id: Int
        }

        """aggregate max on columns"""
        type contract_farms_v2_allfarms_max_fields {
        address: String
        factory: Int
        id: Int
        }

        """aggregate min on columns"""
        type contract_farms_v2_allfarms_min_fields {
        address: String
        factory: Int
        id: Int
        }

        """
        response of any mutation on the table "contract_farms_v2_allfarms"
        """
        type contract_farms_v2_allfarms_mutation_response {
        """number of rows affected by the mutation"""
        affected_rows: Int!

        """data from the rows affected by the mutation"""
        returning: [contract_farms_v2_allfarms!]!
        }

        """
        on_conflict condition type for table "contract_farms_v2_allfarms"
        """
        input contract_farms_v2_allfarms_on_conflict {
        constraInt: contract_farms_v2_allfarms_constraInt!
        update_columns: [contract_farms_v2_allfarms_update_column!]! = []
        where: contract_farms_v2_allfarms_bool_exp
        }

        """
        Ordering options when selecting data from "contract_farms_v2_allfarms".
        """
        input contract_farms_v2_allfarms_order_by {
        address: order_by
        factory: order_by
        id: order_by
        }

        """primary key columns input for table: contract_farms_v2_allfarms"""
        input contract_farms_v2_allfarms_pk_columns_input {
        id: Int!
        }

        """
        select columns of table "contract_farms_v2_allfarms"
        """
        enum contract_farms_v2_allfarms_select_column {
        """column name"""
        address

        """column name"""
        factory

        """column name"""
        id
        }

        """
        input type for updating data in table "contract_farms_v2_allfarms"
        """
        input contract_farms_v2_allfarms_set_input {
        address: String
        factory: Int
        id: Int
        }

        """aggregate stddev on columns"""
        type contract_farms_v2_allfarms_stddev_fields {
        factory: Float
        id: Float
        }

        """aggregate stddev_pop on columns"""
        type contract_farms_v2_allfarms_stddev_pop_fields {
        factory: Float
        id: Float
        }

        """aggregate stddev_samp on columns"""
        type contract_farms_v2_allfarms_stddev_samp_fields {
        factory: Float
        id: Float
        }

        """
        Streaming cursor of the table "contract_farms_v2_allfarms"
        """
        input contract_farms_v2_allfarms_stream_cursor_input {
        """Stream column input with initial value"""
        initial_value: contract_farms_v2_allfarms_stream_cursor_value_input!

        """cursor ordering"""
        ordering: cursor_ordering
        }

        """Initial value of the column from where the streaming should start"""
        input contract_farms_v2_allfarms_stream_cursor_value_input {
        address: String
        factory: Int
        id: Int
        }

        """aggregate sum on columns"""
        type contract_farms_v2_allfarms_sum_fields {
        factory: Int
        id: Int
        }

        """
        update columns of table "contract_farms_v2_allfarms"
        """
        enum contract_farms_v2_allfarms_update_column {
        """column name"""
        address

        """column name"""
        factory

        """column name"""
        id
        }

        input contract_farms_v2_allfarms_updates {
        """increments the numeric columns with given value of the filtered values"""
        _inc: contract_farms_v2_allfarms_inc_input

        """sets the columns of the filtered rows to the given values"""
        _set: contract_farms_v2_allfarms_set_input

        """filter the rows which have to be updated"""
        where: contract_farms_v2_allfarms_bool_exp!
        }

        """aggregate var_pop on columns"""
        type contract_farms_v2_allfarms_var_pop_fields {
        factory: Float
        id: Float
        }

        """aggregate var_samp on columns"""
        type contract_farms_v2_allfarms_var_samp_fields {
        factory: Float
        id: Float
        }

        """aggregate variance on columns"""
        type contract_farms_v2_allfarms_variance_fields {
        factory: Float
        id: Float
        }

        """
        columns and relationships of "contract_farms_v2_operations"
        """
        type contract_farms_v2_operations {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        block: String
        counter: Int
        errors: String
        eventscount: Int
        gaslimit: Int
        gasused: Int
        hash: String
        hasInternals: Boolean
        id: Int!
        initiator: String
        level: Int
        nonce: Int
        parameter: String
        sender: String
        sendercodehash: Int
        status: String
        storagefee: Int
        storagelimit: Int
        storageused: Int
        target: String
        targetcodehash: Int
        timestamp: Int
        tokentransferscount: Int
        type: String
        }

        """
        aggregated selection of "contract_farms_v2_operations"
        """
        type contract_farms_v2_operations_aggregate {
        aggregate: contract_farms_v2_operations_aggregate_fields
        nodes: [contract_farms_v2_operations!]!
        }

        """
        aggregate fields of "contract_farms_v2_operations"
        """
        type contract_farms_v2_operations_aggregate_fields {
        avg: contract_farms_v2_operations_avg_fields
        count(columns: [contract_farms_v2_operations_select_column!], distinct: Boolean): Int!
        max: contract_farms_v2_operations_max_fields
        min: contract_farms_v2_operations_min_fields
        stddev: contract_farms_v2_operations_stddev_fields
        stddev_pop: contract_farms_v2_operations_stddev_pop_fields
        stddev_samp: contract_farms_v2_operations_stddev_samp_fields
        sum: contract_farms_v2_operations_sum_fields
        var_pop: contract_farms_v2_operations_var_pop_fields
        var_samp: contract_farms_v2_operations_var_samp_fields
        variance: contract_farms_v2_operations_variance_fields
        }

        """aggregate avg on columns"""
        type contract_farms_v2_operations_avg_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """
        Boolean expression to filter rows from the table "contract_farms_v2_operations". All fields are combined with a logical 'AND'.
        """
        input contract_farms_v2_operations_bool_exp {
        _and: [contract_farms_v2_operations_bool_exp!]
        _not: contract_farms_v2_operations_bool_exp
        _or: [contract_farms_v2_operations_bool_exp!]
        allocationfee: Int_comparison_exp
        amount: Int_comparison_exp
        bakerfee: Int_comparison_exp
        block: String_comparison_exp
        counter: Int_comparison_exp
        errors: String_comparison_exp
        eventscount: Int_comparison_exp
        gaslimit: Int_comparison_exp
        gasused: Int_comparison_exp
        hash: String_comparison_exp
        hasInternals: Boolean_comparison_exp
        id: Int_comparison_exp
        initiator: String_comparison_exp
        level: Int_comparison_exp
        nonce: Int_comparison_exp
        parameter: String_comparison_exp
        sender: String_comparison_exp
        sendercodehash: Int_comparison_exp
        status: String_comparison_exp
        storagefee: Int_comparison_exp
        storagelimit: Int_comparison_exp
        storageused: Int_comparison_exp
        target: String_comparison_exp
        targetcodehash: Int_comparison_exp
        timestamp: Int_comparison_exp
        tokentransferscount: Int_comparison_exp
        type: String_comparison_exp
        }

        """
        unique or primary key constraInts on table "contract_farms_v2_operations"
        """
        enum contract_farms_v2_operations_constraInt {
        """
        unique or primary key constraInt on columns "id"
        """
        contract_farms_v2_pkey
        }

        """
        input type for incrementing numeric columns in table "contract_farms_v2_operations"
        """
        input contract_farms_v2_operations_inc_input {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        counter: Int
        eventscount: Int
        gaslimit: Int
        gasused: Int
        id: Int
        level: Int
        nonce: Int
        sendercodehash: Int
        storagefee: Int
        storagelimit: Int
        storageused: Int
        targetcodehash: Int
        tokentransferscount: Int
        }

        """
        input type for inserting data Into table "contract_farms_v2_operations"
        """
        input contract_farms_v2_operations_insert_input {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        block: String
        counter: Int
        errors: String
        eventscount: Int
        gaslimit: Int
        gasused: Int
        hash: String
        hasInternals: Boolean
        id: Int
        initiator: String
        level: Int
        nonce: Int
        parameter: String
        sender: String
        sendercodehash: Int
        status: String
        storagefee: Int
        storagelimit: Int
        storageused: Int
        target: String
        targetcodehash: Int
        timestamp: Int
        tokentransferscount: Int
        type: String
        }

        """aggregate max on columns"""
        type contract_farms_v2_operations_max_fields {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        block: String
        counter: Int
        errors: String
        eventscount: Int
        gaslimit: Int
        gasused: Int
        hash: String
        id: Int
        initiator: String
        level: Int
        nonce: Int
        parameter: String
        sender: String
        sendercodehash: Int
        status: String
        storagefee: Int
        storagelimit: Int
        storageused: Int
        target: String
        targetcodehash: Int
        timestamp: Int
        tokentransferscount: Int
        type: String
        }

        """aggregate min on columns"""
        type contract_farms_v2_operations_min_fields {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        block: String
        counter: Int
        errors: String
        eventscount: Int
        gaslimit: Int
        gasused: Int
        hash: String
        id: Int
        initiator: String
        level: Int
        nonce: Int
        parameter: String
        sender: String
        sendercodehash: Int
        status: String
        storagefee: Int
        storagelimit: Int
        storageused: Int
        target: String
        targetcodehash: Int
        timestamp: Int
        tokentransferscount: Int
        type: String
        }

        """
        response of any mutation on the table "contract_farms_v2_operations"
        """
        type contract_farms_v2_operations_mutation_response {
        """number of rows affected by the mutation"""
        affected_rows: Int!

        """data from the rows affected by the mutation"""
        returning: [contract_farms_v2_operations!]!
        }

        """
        on_conflict condition type for table "contract_farms_v2_operations"
        """
        input contract_farms_v2_operations_on_conflict {
        constraInt: contract_farms_v2_operations_constraInt!
        update_columns: [contract_farms_v2_operations_update_column!]! = []
        where: contract_farms_v2_operations_bool_exp
        }

        """
        Ordering options when selecting data from "contract_farms_v2_operations".
        """
        input contract_farms_v2_operations_order_by {
        allocationfee: order_by
        amount: order_by
        bakerfee: order_by
        block: order_by
        counter: order_by
        errors: order_by
        eventscount: order_by
        gaslimit: order_by
        gasused: order_by
        hash: order_by
        hasInternals: order_by
        id: order_by
        initiator: order_by
        level: order_by
        nonce: order_by
        parameter: order_by
        sender: order_by
        sendercodehash: order_by
        status: order_by
        storagefee: order_by
        storagelimit: order_by
        storageused: order_by
        target: order_by
        targetcodehash: order_by
        timestamp: order_by
        tokentransferscount: order_by
        type: order_by
        }

        """primary key columns input for table: contract_farms_v2_operations"""
        input contract_farms_v2_operations_pk_columns_input {
        id: Int!
        }

        """
        select columns of table "contract_farms_v2_operations"
        """
        enum contract_farms_v2_operations_select_column {
        """column name"""
        allocationfee

        """column name"""
        amount

        """column name"""
        bakerfee

        """column name"""
        block

        """column name"""
        counter

        """column name"""
        errors

        """column name"""
        eventscount

        """column name"""
        gaslimit

        """column name"""
        gasused

        """column name"""
        hash

        """column name"""
        hasInternals

        """column name"""
        id

        """column name"""
        initiator

        """column name"""
        level

        """column name"""
        nonce

        """column name"""
        parameter

        """column name"""
        sender

        """column name"""
        sendercodehash

        """column name"""
        status

        """column name"""
        storagefee

        """column name"""
        storagelimit

        """column name"""
        storageused

        """column name"""
        target

        """column name"""
        targetcodehash

        """column name"""
        timestamp

        """column name"""
        tokentransferscount

        """column name"""
        type
        }

        """
        input type for updating data in table "contract_farms_v2_operations"
        """
        input contract_farms_v2_operations_set_input {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        block: String
        counter: Int
        errors: String
        eventscount: Int
        gaslimit: Int
        gasused: Int
        hash: String
        hasInternals: Boolean
        id: Int
        initiator: String
        level: Int
        nonce: Int
        parameter: String
        sender: String
        sendercodehash: Int
        status: String
        storagefee: Int
        storagelimit: Int
        storageused: Int
        target: String
        targetcodehash: Int
        timestamp: Int
        tokentransferscount: Int
        type: String
        }

        """aggregate stddev on columns"""
        type contract_farms_v2_operations_stddev_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """aggregate stddev_pop on columns"""
        type contract_farms_v2_operations_stddev_pop_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """aggregate stddev_samp on columns"""
        type contract_farms_v2_operations_stddev_samp_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """
        Streaming cursor of the table "contract_farms_v2_operations"
        """
        input contract_farms_v2_operations_stream_cursor_input {
        """Stream column input with initial value"""
        initial_value: contract_farms_v2_operations_stream_cursor_value_input!

        """cursor ordering"""
        ordering: cursor_ordering
        }

        """Initial value of the column from where the streaming should start"""
        input contract_farms_v2_operations_stream_cursor_value_input {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        block: String
        counter: Int
        errors: String
        eventscount: Int
        gaslimit: Int
        gasused: Int
        hash: String
        hasInternals: Boolean
        id: Int
        initiator: String
        level: Int
        nonce: Int
        parameter: String
        sender: String
        sendercodehash: Int
        status: String
        storagefee: Int
        storagelimit: Int
        storageused: Int
        target: String
        targetcodehash: Int
        timestamp: Int
        tokentransferscount: Int
        type: String
        }

        """aggregate sum on columns"""
        type contract_farms_v2_operations_sum_fields {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        counter: Int
        eventscount: Int
        gaslimit: Int
        gasused: Int
        id: Int
        level: Int
        nonce: Int
        sendercodehash: Int
        storagefee: Int
        storagelimit: Int
        storageused: Int
        targetcodehash: Int
        tokentransferscount: Int
        }

        """
        update columns of table "contract_farms_v2_operations"
        """
        enum contract_farms_v2_operations_update_column {
        """column name"""
        allocationfee

        """column name"""
        amount

        """column name"""
        bakerfee

        """column name"""
        block

        """column name"""
        counter

        """column name"""
        errors

        """column name"""
        eventscount

        """column name"""
        gaslimit

        """column name"""
        gasused

        """column name"""
        hash

        """column name"""
        hasInternals

        """column name"""
        id

        """column name"""
        initiator

        """column name"""
        level

        """column name"""
        nonce

        """column name"""
        parameter

        """column name"""
        sender

        """column name"""
        sendercodehash

        """column name"""
        status

        """column name"""
        storagefee

        """column name"""
        storagelimit

        """column name"""
        storageused

        """column name"""
        target

        """column name"""
        targetcodehash

        """column name"""
        timestamp

        """column name"""
        tokentransferscount

        """column name"""
        type
        }

        input contract_farms_v2_operations_updates {
        """increments the numeric columns with given value of the filtered values"""
        _inc: contract_farms_v2_operations_inc_input

        """sets the columns of the filtered rows to the given values"""
        _set: contract_farms_v2_operations_set_input

        """filter the rows which have to be updated"""
        where: contract_farms_v2_operations_bool_exp!
        }

        """aggregate var_pop on columns"""
        type contract_farms_v2_operations_var_pop_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """aggregate var_samp on columns"""
        type contract_farms_v2_operations_var_samp_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """aggregate variance on columns"""
        type contract_farms_v2_operations_variance_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """
        columns and relationships of "contract_farms_v2_storage"
        """
        type contract_farms_v2_storage {
        admin: String
        all_farms_data: Int
        id: Int!
        inverse_farms: Int
        }

        """
        aggregated selection of "contract_farms_v2_storage"
        """
        type contract_farms_v2_storage_aggregate {
        aggregate: contract_farms_v2_storage_aggregate_fields
        nodes: [contract_farms_v2_storage!]!
        }

        """
        aggregate fields of "contract_farms_v2_storage"
        """
        type contract_farms_v2_storage_aggregate_fields {
        avg: contract_farms_v2_storage_avg_fields
        count(columns: [contract_farms_v2_storage_select_column!], distinct: Boolean): Int!
        max: contract_farms_v2_storage_max_fields
        min: contract_farms_v2_storage_min_fields
        stddev: contract_farms_v2_storage_stddev_fields
        stddev_pop: contract_farms_v2_storage_stddev_pop_fields
        stddev_samp: contract_farms_v2_storage_stddev_samp_fields
        sum: contract_farms_v2_storage_sum_fields
        var_pop: contract_farms_v2_storage_var_pop_fields
        var_samp: contract_farms_v2_storage_var_samp_fields
        variance: contract_farms_v2_storage_variance_fields
        }

        """aggregate avg on columns"""
        type contract_farms_v2_storage_avg_fields {
        all_farms_data: Float
        id: Float
        inverse_farms: Float
        }

        """
        Boolean expression to filter rows from the table "contract_farms_v2_storage". All fields are combined with a logical 'AND'.
        """
        input contract_farms_v2_storage_bool_exp {
        _and: [contract_farms_v2_storage_bool_exp!]
        _not: contract_farms_v2_storage_bool_exp
        _or: [contract_farms_v2_storage_bool_exp!]
        admin: String_comparison_exp
        all_farms_data: Int_comparison_exp
        id: Int_comparison_exp
        inverse_farms: Int_comparison_exp
        }

        """
        unique or primary key constraInts on table "contract_farms_v2_storage"
        """
        enum contract_farms_v2_storage_constraInt {
        """
        unique or primary key constraInt on columns "id"
        """
        contract_farms_v2_storage_pkey
        }

        """
        input type for incrementing numeric columns in table "contract_farms_v2_storage"
        """
        input contract_farms_v2_storage_inc_input {
        all_farms_data: Int
        id: Int
        inverse_farms: Int
        }

        """
        input type for inserting data Into table "contract_farms_v2_storage"
        """
        input contract_farms_v2_storage_insert_input {
        admin: String
        all_farms_data: Int
        id: Int
        inverse_farms: Int
        }

        """aggregate max on columns"""
        type contract_farms_v2_storage_max_fields {
        admin: String
        all_farms_data: Int
        id: Int
        inverse_farms: Int
        }

        """aggregate min on columns"""
        type contract_farms_v2_storage_min_fields {
        admin: String
        all_farms_data: Int
        id: Int
        inverse_farms: Int
        }

        """
        response of any mutation on the table "contract_farms_v2_storage"
        """
        type contract_farms_v2_storage_mutation_response {
        """number of rows affected by the mutation"""
        affected_rows: Int!

        """data from the rows affected by the mutation"""
        returning: [contract_farms_v2_storage!]!
        }

        """
        on_conflict condition type for table "contract_farms_v2_storage"
        """
        input contract_farms_v2_storage_on_conflict {
        constraInt: contract_farms_v2_storage_constraInt!
        update_columns: [contract_farms_v2_storage_update_column!]! = []
        where: contract_farms_v2_storage_bool_exp
        }

        """Ordering options when selecting data from "contract_farms_v2_storage"."""
        input contract_farms_v2_storage_order_by {
        admin: order_by
        all_farms_data: order_by
        id: order_by
        inverse_farms: order_by
        }

        """primary key columns input for table: contract_farms_v2_storage"""
        input contract_farms_v2_storage_pk_columns_input {
        id: Int!
        }

        """
        select columns of table "contract_farms_v2_storage"
        """
        enum contract_farms_v2_storage_select_column {
        """column name"""
        admin

        """column name"""
        all_farms_data

        """column name"""
        id

        """column name"""
        inverse_farms
        }

        """
        input type for updating data in table "contract_farms_v2_storage"
        """
        input contract_farms_v2_storage_set_input {
        admin: String
        all_farms_data: Int
        id: Int
        inverse_farms: Int
        }

        """aggregate stddev on columns"""
        type contract_farms_v2_storage_stddev_fields {
        all_farms_data: Float
        id: Float
        inverse_farms: Float
        }

        """aggregate stddev_pop on columns"""
        type contract_farms_v2_storage_stddev_pop_fields {
        all_farms_data: Float
        id: Float
        inverse_farms: Float
        }

        """aggregate stddev_samp on columns"""
        type contract_farms_v2_storage_stddev_samp_fields {
        all_farms_data: Float
        id: Float
        inverse_farms: Float
        }

        """
        Streaming cursor of the table "contract_farms_v2_storage"
        """
        input contract_farms_v2_storage_stream_cursor_input {
        """Stream column input with initial value"""
        initial_value: contract_farms_v2_storage_stream_cursor_value_input!

        """cursor ordering"""
        ordering: cursor_ordering
        }

        """Initial value of the column from where the streaming should start"""
        input contract_farms_v2_storage_stream_cursor_value_input {
        admin: String
        all_farms_data: Int
        id: Int
        inverse_farms: Int
        }

        """aggregate sum on columns"""
        type contract_farms_v2_storage_sum_fields {
        all_farms_data: Int
        id: Int
        inverse_farms: Int
        }

        """
        update columns of table "contract_farms_v2_storage"
        """
        enum contract_farms_v2_storage_update_column {
        """column name"""
        admin

        """column name"""
        all_farms_data

        """column name"""
        id

        """column name"""
        inverse_farms
        }

        input contract_farms_v2_storage_updates {
        """increments the numeric columns with given value of the filtered values"""
        _inc: contract_farms_v2_storage_inc_input

        """sets the columns of the filtered rows to the given values"""
        _set: contract_farms_v2_storage_set_input

        """filter the rows which have to be updated"""
        where: contract_farms_v2_storage_bool_exp!
        }

        """aggregate var_pop on columns"""
        type contract_farms_v2_storage_var_pop_fields {
        all_farms_data: Float
        id: Float
        inverse_farms: Float
        }

        """aggregate var_samp on columns"""
        type contract_farms_v2_storage_var_samp_fields {
        all_farms_data: Float
        id: Float
        inverse_farms: Float
        }

        """aggregate variance on columns"""
        type contract_farms_v2_storage_variance_fields {
        all_farms_data: Float
        id: Float
        inverse_farms: Float
        }

        """
        columns and relationships of "contract_staking_smak_operations"
        """
        type contract_staking_smak_operations {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        block: String
        counter: Int
        errors: String
        eventscount: Int
        gaslimit: Int
        gasused: Int
        hash: String
        hasInternals: Boolean
        id: Int!
        initiator: String
        level: Int
        nonce: Int
        parameter: String
        sender: String
        sendercodehash: Int
        status: String
        storagefee: Int
        storagelimit: Int
        storageused: Int
        target: String
        targetcodehash: Int
        timestamp: Int
        tokentransferscount: Int
        type: String
        }

        """
        aggregated selection of "contract_staking_smak_operations"
        """
        type contract_staking_smak_operations_aggregate {
        aggregate: contract_staking_smak_operations_aggregate_fields
        nodes: [contract_staking_smak_operations!]!
        }

        """
        aggregate fields of "contract_staking_smak_operations"
        """
        type contract_staking_smak_operations_aggregate_fields {
        avg: contract_staking_smak_operations_avg_fields
        count(columns: [contract_staking_smak_operations_select_column!], distinct: Boolean): Int!
        max: contract_staking_smak_operations_max_fields
        min: contract_staking_smak_operations_min_fields
        stddev: contract_staking_smak_operations_stddev_fields
        stddev_pop: contract_staking_smak_operations_stddev_pop_fields
        stddev_samp: contract_staking_smak_operations_stddev_samp_fields
        sum: contract_staking_smak_operations_sum_fields
        var_pop: contract_staking_smak_operations_var_pop_fields
        var_samp: contract_staking_smak_operations_var_samp_fields
        variance: contract_staking_smak_operations_variance_fields
        }

        """aggregate avg on columns"""
        type contract_staking_smak_operations_avg_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """
        Boolean expression to filter rows from the table "contract_staking_smak_operations". All fields are combined with a logical 'AND'.
        """
        input contract_staking_smak_operations_bool_exp {
        _and: [contract_staking_smak_operations_bool_exp!]
        _not: contract_staking_smak_operations_bool_exp
        _or: [contract_staking_smak_operations_bool_exp!]
        allocationfee: Int_comparison_exp
        amount: Int_comparison_exp
        bakerfee: Int_comparison_exp
        block: String_comparison_exp
        counter: Int_comparison_exp
        errors: String_comparison_exp
        eventscount: Int_comparison_exp
        gaslimit: Int_comparison_exp
        gasused: Int_comparison_exp
        hash: String_comparison_exp
        hasInternals: Boolean_comparison_exp
        id: Int_comparison_exp
        initiator: String_comparison_exp
        level: Int_comparison_exp
        nonce: Int_comparison_exp
        parameter: String_comparison_exp
        sender: String_comparison_exp
        sendercodehash: Int_comparison_exp
        status: String_comparison_exp
        storagefee: Int_comparison_exp
        storagelimit: Int_comparison_exp
        storageused: Int_comparison_exp
        target: String_comparison_exp
        targetcodehash: Int_comparison_exp
        timestamp: Int_comparison_exp
        tokentransferscount: Int_comparison_exp
        type: String_comparison_exp
        }

        """
        unique or primary key constraInts on table "contract_staking_smak_operations"
        """
        enum contract_staking_smak_operations_constraInt {
        """
        unique or primary key constraInt on columns "id"
        """
        contract_staking_smak_operations_pkey
        }

        """
        input type for incrementing numeric columns in table "contract_staking_smak_operations"
        """
        input contract_staking_smak_operations_inc_input {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        counter: Int
        eventscount: Int
        gaslimit: Int
        gasused: Int
        id: Int
        level: Int
        nonce: Int
        sendercodehash: Int
        storagefee: Int
        storagelimit: Int
        storageused: Int
        targetcodehash: Int
        tokentransferscount: Int
        }

        """
        input type for inserting data Into table "contract_staking_smak_operations"
        """
        input contract_staking_smak_operations_insert_input {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        block: String
        counter: Int
        errors: String
        eventscount: Int
        gaslimit: Int
        gasused: Int
        hash: String
        hasInternals: Boolean
        id: Int
        initiator: String
        level: Int
        nonce: Int
        parameter: String
        sender: String
        sendercodehash: Int
        status: String
        storagefee: Int
        storagelimit: Int
        storageused: Int
        target: String
        targetcodehash: Int
        timestamp: Int
        tokentransferscount: Int
        type: String
        }

        """aggregate max on columns"""
        type contract_staking_smak_operations_max_fields {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        block: String
        counter: Int
        errors: String
        eventscount: Int
        gaslimit: Int
        gasused: Int
        hash: String
        id: Int
        initiator: String
        level: Int
        nonce: Int
        parameter: String
        sender: String
        sendercodehash: Int
        status: String
        storagefee: Int
        storagelimit: Int
        storageused: Int
        target: String
        targetcodehash: Int
        timestamp: Int
        tokentransferscount: Int
        type: String
        }

        """aggregate min on columns"""
        type contract_staking_smak_operations_min_fields {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        block: String
        counter: Int
        errors: String
        eventscount: Int
        gaslimit: Int
        gasused: Int
        hash: String
        id: Int
        initiator: String
        level: Int
        nonce: Int
        parameter: String
        sender: String
        sendercodehash: Int
        status: String
        storagefee: Int
        storagelimit: Int
        storageused: Int
        target: String
        targetcodehash: Int
        timestamp: Int
        tokentransferscount: Int
        type: String
        }

        """
        response of any mutation on the table "contract_staking_smak_operations"
        """
        type contract_staking_smak_operations_mutation_response {
        """number of rows affected by the mutation"""
        affected_rows: Int!

        """data from the rows affected by the mutation"""
        returning: [contract_staking_smak_operations!]!
        }

        """
        on_conflict condition type for table "contract_staking_smak_operations"
        """
        input contract_staking_smak_operations_on_conflict {
        constraInt: contract_staking_smak_operations_constraInt!
        update_columns: [contract_staking_smak_operations_update_column!]! = []
        where: contract_staking_smak_operations_bool_exp
        }

        """
        Ordering options when selecting data from "contract_staking_smak_operations".
        """
        input contract_staking_smak_operations_order_by {
        allocationfee: order_by
        amount: order_by
        bakerfee: order_by
        block: order_by
        counter: order_by
        errors: order_by
        eventscount: order_by
        gaslimit: order_by
        gasused: order_by
        hash: order_by
        hasInternals: order_by
        id: order_by
        initiator: order_by
        level: order_by
        nonce: order_by
        parameter: order_by
        sender: order_by
        sendercodehash: order_by
        status: order_by
        storagefee: order_by
        storagelimit: order_by
        storageused: order_by
        target: order_by
        targetcodehash: order_by
        timestamp: order_by
        tokentransferscount: order_by
        type: order_by
        }

        """primary key columns input for table: contract_staking_smak_operations"""
        input contract_staking_smak_operations_pk_columns_input {
        id: Int!
        }

        """
        select columns of table "contract_staking_smak_operations"
        """
        enum contract_staking_smak_operations_select_column {
        """column name"""
        allocationfee

        """column name"""
        amount

        """column name"""
        bakerfee

        """column name"""
        block

        """column name"""
        counter

        """column name"""
        errors

        """column name"""
        eventscount

        """column name"""
        gaslimit

        """column name"""
        gasused

        """column name"""
        hash

        """column name"""
        hasInternals

        """column name"""
        id

        """column name"""
        initiator

        """column name"""
        level

        """column name"""
        nonce

        """column name"""
        parameter

        """column name"""
        sender

        """column name"""
        sendercodehash

        """column name"""
        status

        """column name"""
        storagefee

        """column name"""
        storagelimit

        """column name"""
        storageused

        """column name"""
        target

        """column name"""
        targetcodehash

        """column name"""
        timestamp

        """column name"""
        tokentransferscount

        """column name"""
        type
        }

        """
        input type for updating data in table "contract_staking_smak_operations"
        """
        input contract_staking_smak_operations_set_input {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        block: String
        counter: Int
        errors: String
        eventscount: Int
        gaslimit: Int
        gasused: Int
        hash: String
        hasInternals: Boolean
        id: Int
        initiator: String
        level: Int
        nonce: Int
        parameter: String
        sender: String
        sendercodehash: Int
        status: String
        storagefee: Int
        storagelimit: Int
        storageused: Int
        target: String
        targetcodehash: Int
        timestamp: Int
        tokentransferscount: Int
        type: String
        }

        """aggregate stddev on columns"""
        type contract_staking_smak_operations_stddev_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """aggregate stddev_pop on columns"""
        type contract_staking_smak_operations_stddev_pop_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """aggregate stddev_samp on columns"""
        type contract_staking_smak_operations_stddev_samp_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """
        Streaming cursor of the table "contract_staking_smak_operations"
        """
        input contract_staking_smak_operations_stream_cursor_input {
        """Stream column input with initial value"""
        initial_value: contract_staking_smak_operations_stream_cursor_value_input!

        """cursor ordering"""
        ordering: cursor_ordering
        }

        """Initial value of the column from where the streaming should start"""
        input contract_staking_smak_operations_stream_cursor_value_input {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        block: String
        counter: Int
        errors: String
        eventscount: Int
        gaslimit: Int
        gasused: Int
        hash: String
        hasInternals: Boolean
        id: Int
        initiator: String
        level: Int
        nonce: Int
        parameter: String
        sender: String
        sendercodehash: Int
        status: String
        storagefee: Int
        storagelimit: Int
        storageused: Int
        target: String
        targetcodehash: Int
        timestamp: Int
        tokentransferscount: Int
        type: String
        }

        """aggregate sum on columns"""
        type contract_staking_smak_operations_sum_fields {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        counter: Int
        eventscount: Int
        gaslimit: Int
        gasused: Int
        id: Int
        level: Int
        nonce: Int
        sendercodehash: Int
        storagefee: Int
        storagelimit: Int
        storageused: Int
        targetcodehash: Int
        tokentransferscount: Int
        }

        """
        update columns of table "contract_staking_smak_operations"
        """
        enum contract_staking_smak_operations_update_column {
        """column name"""
        allocationfee

        """column name"""
        amount

        """column name"""
        bakerfee

        """column name"""
        block

        """column name"""
        counter

        """column name"""
        errors

        """column name"""
        eventscount

        """column name"""
        gaslimit

        """column name"""
        gasused

        """column name"""
        hash

        """column name"""
        hasInternals

        """column name"""
        id

        """column name"""
        initiator

        """column name"""
        level

        """column name"""
        nonce

        """column name"""
        parameter

        """column name"""
        sender

        """column name"""
        sendercodehash

        """column name"""
        status

        """column name"""
        storagefee

        """column name"""
        storagelimit

        """column name"""
        storageused

        """column name"""
        target

        """column name"""
        targetcodehash

        """column name"""
        timestamp

        """column name"""
        tokentransferscount

        """column name"""
        type
        }

        input contract_staking_smak_operations_updates {
        """increments the numeric columns with given value of the filtered values"""
        _inc: contract_staking_smak_operations_inc_input

        """sets the columns of the filtered rows to the given values"""
        _set: contract_staking_smak_operations_set_input

        """filter the rows which have to be updated"""
        where: contract_staking_smak_operations_bool_exp!
        }

        """aggregate var_pop on columns"""
        type contract_staking_smak_operations_var_pop_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """aggregate var_samp on columns"""
        type contract_staking_smak_operations_var_samp_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """aggregate variance on columns"""
        type contract_staking_smak_operations_variance_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """
        columns and relationships of "contract_staking_smak_storage"
        """
        type contract_staking_smak_storage {
        addressid: Int
        admin: String
        can_set_storage: Boolean
        fa12tokencontract: String
        id: Int!
        maxvaluesnb: String
        metadata: Int
        numberofstakers: String
        redeemedrewards: Int
        reserve: String
        stakeflexlength: String
        stakinghistory: Int
        totalredeemedrewards: String
        userstakeflexpack: Int
        userstakelockpack: Int
        votingcontract: String
        }

        """
        aggregated selection of "contract_staking_smak_storage"
        """
        type contract_staking_smak_storage_aggregate {
        aggregate: contract_staking_smak_storage_aggregate_fields
        nodes: [contract_staking_smak_storage!]!
        }

        """
        aggregate fields of "contract_staking_smak_storage"
        """
        type contract_staking_smak_storage_aggregate_fields {
        avg: contract_staking_smak_storage_avg_fields
        count(columns: [contract_staking_smak_storage_select_column!], distinct: Boolean): Int!
        max: contract_staking_smak_storage_max_fields
        min: contract_staking_smak_storage_min_fields
        stddev: contract_staking_smak_storage_stddev_fields
        stddev_pop: contract_staking_smak_storage_stddev_pop_fields
        stddev_samp: contract_staking_smak_storage_stddev_samp_fields
        sum: contract_staking_smak_storage_sum_fields
        var_pop: contract_staking_smak_storage_var_pop_fields
        var_samp: contract_staking_smak_storage_var_samp_fields
        variance: contract_staking_smak_storage_variance_fields
        }

        """aggregate avg on columns"""
        type contract_staking_smak_storage_avg_fields {
        addressid: Float
        id: Float
        metadata: Float
        redeemedrewards: Float
        stakinghistory: Float
        userstakeflexpack: Float
        userstakelockpack: Float
        }

        """
        Boolean expression to filter rows from the table "contract_staking_smak_storage". All fields are combined with a logical 'AND'.
        """
        input contract_staking_smak_storage_bool_exp {
        _and: [contract_staking_smak_storage_bool_exp!]
        _not: contract_staking_smak_storage_bool_exp
        _or: [contract_staking_smak_storage_bool_exp!]
        addressid: Int_comparison_exp
        admin: String_comparison_exp
        can_set_storage: Boolean_comparison_exp
        fa12tokencontract: String_comparison_exp
        id: Int_comparison_exp
        maxvaluesnb: String_comparison_exp
        metadata: Int_comparison_exp
        numberofstakers: String_comparison_exp
        redeemedrewards: Int_comparison_exp
        reserve: String_comparison_exp
        stakeflexlength: String_comparison_exp
        stakinghistory: Int_comparison_exp
        totalredeemedrewards: String_comparison_exp
        userstakeflexpack: Int_comparison_exp
        userstakelockpack: Int_comparison_exp
        votingcontract: String_comparison_exp
        }

        """
        unique or primary key constraInts on table "contract_staking_smak_storage"
        """
        enum contract_staking_smak_storage_constraInt {
        """
        unique or primary key constraInt on columns "id"
        """
        contract_staking_smak_storage_pkey
        }

        """
        input type for incrementing numeric columns in table "contract_staking_smak_storage"
        """
        input contract_staking_smak_storage_inc_input {
        addressid: Int
        id: Int
        metadata: Int
        redeemedrewards: Int
        stakinghistory: Int
        userstakeflexpack: Int
        userstakelockpack: Int
        }

        """
        input type for inserting data Into table "contract_staking_smak_storage"
        """
        input contract_staking_smak_storage_insert_input {
        addressid: Int
        admin: String
        can_set_storage: Boolean
        fa12tokencontract: String
        id: Int
        maxvaluesnb: String
        metadata: Int
        numberofstakers: String
        redeemedrewards: Int
        reserve: String
        stakeflexlength: String
        stakinghistory: Int
        totalredeemedrewards: String
        userstakeflexpack: Int
        userstakelockpack: Int
        votingcontract: String
        }

        """aggregate max on columns"""
        type contract_staking_smak_storage_max_fields {
        addressid: Int
        admin: String
        fa12tokencontract: String
        id: Int
        maxvaluesnb: String
        metadata: Int
        numberofstakers: String
        redeemedrewards: Int
        reserve: String
        stakeflexlength: String
        stakinghistory: Int
        totalredeemedrewards: String
        userstakeflexpack: Int
        userstakelockpack: Int
        votingcontract: String
        }

        """aggregate min on columns"""
        type contract_staking_smak_storage_min_fields {
        addressid: Int
        admin: String
        fa12tokencontract: String
        id: Int
        maxvaluesnb: String
        metadata: Int
        numberofstakers: String
        redeemedrewards: Int
        reserve: String
        stakeflexlength: String
        stakinghistory: Int
        totalredeemedrewards: String
        userstakeflexpack: Int
        userstakelockpack: Int
        votingcontract: String
        }

        """
        response of any mutation on the table "contract_staking_smak_storage"
        """
        type contract_staking_smak_storage_mutation_response {
        """number of rows affected by the mutation"""
        affected_rows: Int!

        """data from the rows affected by the mutation"""
        returning: [contract_staking_smak_storage!]!
        }

        """
        on_conflict condition type for table "contract_staking_smak_storage"
        """
        input contract_staking_smak_storage_on_conflict {
        constraInt: contract_staking_smak_storage_constraInt!
        update_columns: [contract_staking_smak_storage_update_column!]! = []
        where: contract_staking_smak_storage_bool_exp
        }

        """
        Ordering options when selecting data from "contract_staking_smak_storage".
        """
        input contract_staking_smak_storage_order_by {
        addressid: order_by
        admin: order_by
        can_set_storage: order_by
        fa12tokencontract: order_by
        id: order_by
        maxvaluesnb: order_by
        metadata: order_by
        numberofstakers: order_by
        redeemedrewards: order_by
        reserve: order_by
        stakeflexlength: order_by
        stakinghistory: order_by
        totalredeemedrewards: order_by
        userstakeflexpack: order_by
        userstakelockpack: order_by
        votingcontract: order_by
        }

        """primary key columns input for table: contract_staking_smak_storage"""
        input contract_staking_smak_storage_pk_columns_input {
        id: Int!
        }

        """
        select columns of table "contract_staking_smak_storage"
        """
        enum contract_staking_smak_storage_select_column {
        """column name"""
        addressid

        """column name"""
        admin

        """column name"""
        can_set_storage

        """column name"""
        fa12tokencontract

        """column name"""
        id

        """column name"""
        maxvaluesnb

        """column name"""
        metadata

        """column name"""
        numberofstakers

        """column name"""
        redeemedrewards

        """column name"""
        reserve

        """column name"""
        stakeflexlength

        """column name"""
        stakinghistory

        """column name"""
        totalredeemedrewards

        """column name"""
        userstakeflexpack

        """column name"""
        userstakelockpack

        """column name"""
        votingcontract
        }

        """
        input type for updating data in table "contract_staking_smak_storage"
        """
        input contract_staking_smak_storage_set_input {
        addressid: Int
        admin: String
        can_set_storage: Boolean
        fa12tokencontract: String
        id: Int
        maxvaluesnb: String
        metadata: Int
        numberofstakers: String
        redeemedrewards: Int
        reserve: String
        stakeflexlength: String
        stakinghistory: Int
        totalredeemedrewards: String
        userstakeflexpack: Int
        userstakelockpack: Int
        votingcontract: String
        }

        """aggregate stddev on columns"""
        type contract_staking_smak_storage_stddev_fields {
        addressid: Float
        id: Float
        metadata: Float
        redeemedrewards: Float
        stakinghistory: Float
        userstakeflexpack: Float
        userstakelockpack: Float
        }

        """aggregate stddev_pop on columns"""
        type contract_staking_smak_storage_stddev_pop_fields {
        addressid: Float
        id: Float
        metadata: Float
        redeemedrewards: Float
        stakinghistory: Float
        userstakeflexpack: Float
        userstakelockpack: Float
        }

        """aggregate stddev_samp on columns"""
        type contract_staking_smak_storage_stddev_samp_fields {
        addressid: Float
        id: Float
        metadata: Float
        redeemedrewards: Float
        stakinghistory: Float
        userstakeflexpack: Float
        userstakelockpack: Float
        }

        """
        Streaming cursor of the table "contract_staking_smak_storage"
        """
        input contract_staking_smak_storage_stream_cursor_input {
        """Stream column input with initial value"""
        initial_value: contract_staking_smak_storage_stream_cursor_value_input!

        """cursor ordering"""
        ordering: cursor_ordering
        }

        """Initial value of the column from where the streaming should start"""
        input contract_staking_smak_storage_stream_cursor_value_input {
        addressid: Int
        admin: String
        can_set_storage: Boolean
        fa12tokencontract: String
        id: Int
        maxvaluesnb: String
        metadata: Int
        numberofstakers: String
        redeemedrewards: Int
        reserve: String
        stakeflexlength: String
        stakinghistory: Int
        totalredeemedrewards: String
        userstakeflexpack: Int
        userstakelockpack: Int
        votingcontract: String
        }

        """aggregate sum on columns"""
        type contract_staking_smak_storage_sum_fields {
        addressid: Int
        id: Int
        metadata: Int
        redeemedrewards: Int
        stakinghistory: Int
        userstakeflexpack: Int
        userstakelockpack: Int
        }

        """
        update columns of table "contract_staking_smak_storage"
        """
        enum contract_staking_smak_storage_update_column {
        """column name"""
        addressid

        """column name"""
        admin

        """column name"""
        can_set_storage

        """column name"""
        fa12tokencontract

        """column name"""
        id

        """column name"""
        maxvaluesnb

        """column name"""
        metadata

        """column name"""
        numberofstakers

        """column name"""
        redeemedrewards

        """column name"""
        reserve

        """column name"""
        stakeflexlength

        """column name"""
        stakinghistory

        """column name"""
        totalredeemedrewards

        """column name"""
        userstakeflexpack

        """column name"""
        userstakelockpack

        """column name"""
        votingcontract
        }

        input contract_staking_smak_storage_updates {
        """increments the numeric columns with given value of the filtered values"""
        _inc: contract_staking_smak_storage_inc_input

        """sets the columns of the filtered rows to the given values"""
        _set: contract_staking_smak_storage_set_input

        """filter the rows which have to be updated"""
        where: contract_staking_smak_storage_bool_exp!
        }

        """aggregate var_pop on columns"""
        type contract_staking_smak_storage_var_pop_fields {
        addressid: Float
        id: Float
        metadata: Float
        redeemedrewards: Float
        stakinghistory: Float
        userstakeflexpack: Float
        userstakelockpack: Float
        }

        """aggregate var_samp on columns"""
        type contract_staking_smak_storage_var_samp_fields {
        addressid: Float
        id: Float
        metadata: Float
        redeemedrewards: Float
        stakinghistory: Float
        userstakeflexpack: Float
        userstakelockpack: Float
        }

        """aggregate variance on columns"""
        type contract_staking_smak_storage_variance_fields {
        addressid: Float
        id: Float
        metadata: Float
        redeemedrewards: Float
        stakinghistory: Float
        userstakeflexpack: Float
        userstakelockpack: Float
        }

        """
        columns and relationships of "contract_token_anti_operations"
        """
        type contract_token_anti_operations {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        block: String
        counter: Int
        errors: String
        eventscount: Int
        gaslimit: Int
        gasused: Int
        hash: String
        hasInternals: Boolean
        id: Int!
        initiator: String
        level: Int
        nonce: Int
        parameter: String
        sender: String
        sendercodehash: Int
        status: String
        storagefee: Int
        storagelimit: Int
        storageused: Int
        target: String
        targetcodehash: Int
        timestamp: Int
        tokentransferscount: Int
        type: String
        }

        """
        aggregated selection of "contract_token_anti_operations"
        """
        type contract_token_anti_operations_aggregate {
        aggregate: contract_token_anti_operations_aggregate_fields
        nodes: [contract_token_anti_operations!]!
        }

        """
        aggregate fields of "contract_token_anti_operations"
        """
        type contract_token_anti_operations_aggregate_fields {
        avg: contract_token_anti_operations_avg_fields
        count(columns: [contract_token_anti_operations_select_column!], distinct: Boolean): Int!
        max: contract_token_anti_operations_max_fields
        min: contract_token_anti_operations_min_fields
        stddev: contract_token_anti_operations_stddev_fields
        stddev_pop: contract_token_anti_operations_stddev_pop_fields
        stddev_samp: contract_token_anti_operations_stddev_samp_fields
        sum: contract_token_anti_operations_sum_fields
        var_pop: contract_token_anti_operations_var_pop_fields
        var_samp: contract_token_anti_operations_var_samp_fields
        variance: contract_token_anti_operations_variance_fields
        }

        """aggregate avg on columns"""
        type contract_token_anti_operations_avg_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """
        Boolean expression to filter rows from the table "contract_token_anti_operations". All fields are combined with a logical 'AND'.
        """
        input contract_token_anti_operations_bool_exp {
        _and: [contract_token_anti_operations_bool_exp!]
        _not: contract_token_anti_operations_bool_exp
        _or: [contract_token_anti_operations_bool_exp!]
        allocationfee: Int_comparison_exp
        amount: Int_comparison_exp
        bakerfee: Int_comparison_exp
        block: String_comparison_exp
        counter: Int_comparison_exp
        errors: String_comparison_exp
        eventscount: Int_comparison_exp
        gaslimit: Int_comparison_exp
        gasused: Int_comparison_exp
        hash: String_comparison_exp
        hasInternals: Boolean_comparison_exp
        id: Int_comparison_exp
        initiator: String_comparison_exp
        level: Int_comparison_exp
        nonce: Int_comparison_exp
        parameter: String_comparison_exp
        sender: String_comparison_exp
        sendercodehash: Int_comparison_exp
        status: String_comparison_exp
        storagefee: Int_comparison_exp
        storagelimit: Int_comparison_exp
        storageused: Int_comparison_exp
        target: String_comparison_exp
        targetcodehash: Int_comparison_exp
        timestamp: Int_comparison_exp
        tokentransferscount: Int_comparison_exp
        type: String_comparison_exp
        }

        """
        unique or primary key constraInts on table "contract_token_anti_operations"
        """
        enum contract_token_anti_operations_constraInt {
        """
        unique or primary key constraInt on columns "id"
        """
        contract_token_anti_operations_pkey
        }

        """
        input type for incrementing numeric columns in table "contract_token_anti_operations"
        """
        input contract_token_anti_operations_inc_input {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        counter: Int
        eventscount: Int
        gaslimit: Int
        gasused: Int
        id: Int
        level: Int
        nonce: Int
        sendercodehash: Int
        storagefee: Int
        storagelimit: Int
        storageused: Int
        targetcodehash: Int
        tokentransferscount: Int
        }

        """
        input type for inserting data Into table "contract_token_anti_operations"
        """
        input contract_token_anti_operations_insert_input {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        block: String
        counter: Int
        errors: String
        eventscount: Int
        gaslimit: Int
        gasused: Int
        hash: String
        hasInternals: Boolean
        id: Int
        initiator: String
        level: Int
        nonce: Int
        parameter: String
        sender: String
        sendercodehash: Int
        status: String
        storagefee: Int
        storagelimit: Int
        storageused: Int
        target: String
        targetcodehash: Int
        timestamp: Int
        tokentransferscount: Int
        type: String
        }

        """aggregate max on columns"""
        type contract_token_anti_operations_max_fields {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        block: String
        counter: Int
        errors: String
        eventscount: Int
        gaslimit: Int
        gasused: Int
        hash: String
        id: Int
        initiator: String
        level: Int
        nonce: Int
        parameter: String
        sender: String
        sendercodehash: Int
        status: String
        storagefee: Int
        storagelimit: Int
        storageused: Int
        target: String
        targetcodehash: Int
        timestamp: Int
        tokentransferscount: Int
        type: String
        }

        """aggregate min on columns"""
        type contract_token_anti_operations_min_fields {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        block: String
        counter: Int
        errors: String
        eventscount: Int
        gaslimit: Int
        gasused: Int
        hash: String
        id: Int
        initiator: String
        level: Int
        nonce: Int
        parameter: String
        sender: String
        sendercodehash: Int
        status: String
        storagefee: Int
        storagelimit: Int
        storageused: Int
        target: String
        targetcodehash: Int
        timestamp: Int
        tokentransferscount: Int
        type: String
        }

        """
        response of any mutation on the table "contract_token_anti_operations"
        """
        type contract_token_anti_operations_mutation_response {
        """number of rows affected by the mutation"""
        affected_rows: Int!

        """data from the rows affected by the mutation"""
        returning: [contract_token_anti_operations!]!
        }

        """
        on_conflict condition type for table "contract_token_anti_operations"
        """
        input contract_token_anti_operations_on_conflict {
        constraInt: contract_token_anti_operations_constraInt!
        update_columns: [contract_token_anti_operations_update_column!]! = []
        where: contract_token_anti_operations_bool_exp
        }

        """
        Ordering options when selecting data from "contract_token_anti_operations".
        """
        input contract_token_anti_operations_order_by {
        allocationfee: order_by
        amount: order_by
        bakerfee: order_by
        block: order_by
        counter: order_by
        errors: order_by
        eventscount: order_by
        gaslimit: order_by
        gasused: order_by
        hash: order_by
        hasInternals: order_by
        id: order_by
        initiator: order_by
        level: order_by
        nonce: order_by
        parameter: order_by
        sender: order_by
        sendercodehash: order_by
        status: order_by
        storagefee: order_by
        storagelimit: order_by
        storageused: order_by
        target: order_by
        targetcodehash: order_by
        timestamp: order_by
        tokentransferscount: order_by
        type: order_by
        }

        """primary key columns input for table: contract_token_anti_operations"""
        input contract_token_anti_operations_pk_columns_input {
        id: Int!
        }

        """
        select columns of table "contract_token_anti_operations"
        """
        enum contract_token_anti_operations_select_column {
        """column name"""
        allocationfee

        """column name"""
        amount

        """column name"""
        bakerfee

        """column name"""
        block

        """column name"""
        counter

        """column name"""
        errors

        """column name"""
        eventscount

        """column name"""
        gaslimit

        """column name"""
        gasused

        """column name"""
        hash

        """column name"""
        hasInternals

        """column name"""
        id

        """column name"""
        initiator

        """column name"""
        level

        """column name"""
        nonce

        """column name"""
        parameter

        """column name"""
        sender

        """column name"""
        sendercodehash

        """column name"""
        status

        """column name"""
        storagefee

        """column name"""
        storagelimit

        """column name"""
        storageused

        """column name"""
        target

        """column name"""
        targetcodehash

        """column name"""
        timestamp

        """column name"""
        tokentransferscount

        """column name"""
        type
        }

        """
        input type for updating data in table "contract_token_anti_operations"
        """
        input contract_token_anti_operations_set_input {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        block: String
        counter: Int
        errors: String
        eventscount: Int
        gaslimit: Int
        gasused: Int
        hash: String
        hasInternals: Boolean
        id: Int
        initiator: String
        level: Int
        nonce: Int
        parameter: String
        sender: String
        sendercodehash: Int
        status: String
        storagefee: Int
        storagelimit: Int
        storageused: Int
        target: String
        targetcodehash: Int
        timestamp: Int
        tokentransferscount: Int
        type: String
        }

        """aggregate stddev on columns"""
        type contract_token_anti_operations_stddev_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """aggregate stddev_pop on columns"""
        type contract_token_anti_operations_stddev_pop_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """aggregate stddev_samp on columns"""
        type contract_token_anti_operations_stddev_samp_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """
        Streaming cursor of the table "contract_token_anti_operations"
        """
        input contract_token_anti_operations_stream_cursor_input {
        """Stream column input with initial value"""
        initial_value: contract_token_anti_operations_stream_cursor_value_input!

        """cursor ordering"""
        ordering: cursor_ordering
        }

        """Initial value of the column from where the streaming should start"""
        input contract_token_anti_operations_stream_cursor_value_input {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        block: String
        counter: Int
        errors: String
        eventscount: Int
        gaslimit: Int
        gasused: Int
        hash: String
        hasInternals: Boolean
        id: Int
        initiator: String
        level: Int
        nonce: Int
        parameter: String
        sender: String
        sendercodehash: Int
        status: String
        storagefee: Int
        storagelimit: Int
        storageused: Int
        target: String
        targetcodehash: Int
        timestamp: Int
        tokentransferscount: Int
        type: String
        }

        """aggregate sum on columns"""
        type contract_token_anti_operations_sum_fields {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        counter: Int
        eventscount: Int
        gaslimit: Int
        gasused: Int
        id: Int
        level: Int
        nonce: Int
        sendercodehash: Int
        storagefee: Int
        storagelimit: Int
        storageused: Int
        targetcodehash: Int
        tokentransferscount: Int
        }

        """
        update columns of table "contract_token_anti_operations"
        """
        enum contract_token_anti_operations_update_column {
        """column name"""
        allocationfee

        """column name"""
        amount

        """column name"""
        bakerfee

        """column name"""
        block

        """column name"""
        counter

        """column name"""
        errors

        """column name"""
        eventscount

        """column name"""
        gaslimit

        """column name"""
        gasused

        """column name"""
        hash

        """column name"""
        hasInternals

        """column name"""
        id

        """column name"""
        initiator

        """column name"""
        level

        """column name"""
        nonce

        """column name"""
        parameter

        """column name"""
        sender

        """column name"""
        sendercodehash

        """column name"""
        status

        """column name"""
        storagefee

        """column name"""
        storagelimit

        """column name"""
        storageused

        """column name"""
        target

        """column name"""
        targetcodehash

        """column name"""
        timestamp

        """column name"""
        tokentransferscount

        """column name"""
        type
        }

        input contract_token_anti_operations_updates {
        """increments the numeric columns with given value of the filtered values"""
        _inc: contract_token_anti_operations_inc_input

        """sets the columns of the filtered rows to the given values"""
        _set: contract_token_anti_operations_set_input

        """filter the rows which have to be updated"""
        where: contract_token_anti_operations_bool_exp!
        }

        """aggregate var_pop on columns"""
        type contract_token_anti_operations_var_pop_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """aggregate var_samp on columns"""
        type contract_token_anti_operations_var_samp_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """aggregate variance on columns"""
        type contract_token_anti_operations_variance_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """
        columns and relationships of "contract_token_anti_storage"
        """
        type contract_token_anti_storage {
        admin: String
        allowances: String
        burn_address: String
        burned_supply: String
        id: Int!
        initial_supply: String
        ledger: String
        metadata: String
        reserve: String
        token_metadata: String
        total_supply: String
        }

        """
        aggregated selection of "contract_token_anti_storage"
        """
        type contract_token_anti_storage_aggregate {
        aggregate: contract_token_anti_storage_aggregate_fields
        nodes: [contract_token_anti_storage!]!
        }

        """
        aggregate fields of "contract_token_anti_storage"
        """
        type contract_token_anti_storage_aggregate_fields {
        avg: contract_token_anti_storage_avg_fields
        count(columns: [contract_token_anti_storage_select_column!], distinct: Boolean): Int!
        max: contract_token_anti_storage_max_fields
        min: contract_token_anti_storage_min_fields
        stddev: contract_token_anti_storage_stddev_fields
        stddev_pop: contract_token_anti_storage_stddev_pop_fields
        stddev_samp: contract_token_anti_storage_stddev_samp_fields
        sum: contract_token_anti_storage_sum_fields
        var_pop: contract_token_anti_storage_var_pop_fields
        var_samp: contract_token_anti_storage_var_samp_fields
        variance: contract_token_anti_storage_variance_fields
        }

        """aggregate avg on columns"""
        type contract_token_anti_storage_avg_fields {
        id: Float
        }

        """
        Boolean expression to filter rows from the table "contract_token_anti_storage". All fields are combined with a logical 'AND'.
        """
        input contract_token_anti_storage_bool_exp {
        _and: [contract_token_anti_storage_bool_exp!]
        _not: contract_token_anti_storage_bool_exp
        _or: [contract_token_anti_storage_bool_exp!]
        admin: String_comparison_exp
        allowances: String_comparison_exp
        burn_address: String_comparison_exp
        burned_supply: String_comparison_exp
        id: Int_comparison_exp
        initial_supply: String_comparison_exp
        ledger: String_comparison_exp
        metadata: String_comparison_exp
        reserve: String_comparison_exp
        token_metadata: String_comparison_exp
        total_supply: String_comparison_exp
        }

        """
        unique or primary key constraInts on table "contract_token_anti_storage"
        """
        enum contract_token_anti_storage_constraInt {
        """
        unique or primary key constraInt on columns "id"
        """
        contract_token_anti_storage_pkey
        }

        """
        input type for incrementing numeric columns in table "contract_token_anti_storage"
        """
        input contract_token_anti_storage_inc_input {
        id: Int
        }

        """
        input type for inserting data Into table "contract_token_anti_storage"
        """
        input contract_token_anti_storage_insert_input {
        admin: String
        allowances: String
        burn_address: String
        burned_supply: String
        id: Int
        initial_supply: String
        ledger: String
        metadata: String
        reserve: String
        token_metadata: String
        total_supply: String
        }

        """aggregate max on columns"""
        type contract_token_anti_storage_max_fields {
        admin: String
        allowances: String
        burn_address: String
        burned_supply: String
        id: Int
        initial_supply: String
        ledger: String
        metadata: String
        reserve: String
        token_metadata: String
        total_supply: String
        }

        """aggregate min on columns"""
        type contract_token_anti_storage_min_fields {
        admin: String
        allowances: String
        burn_address: String
        burned_supply: String
        id: Int
        initial_supply: String
        ledger: String
        metadata: String
        reserve: String
        token_metadata: String
        total_supply: String
        }

        """
        response of any mutation on the table "contract_token_anti_storage"
        """
        type contract_token_anti_storage_mutation_response {
        """number of rows affected by the mutation"""
        affected_rows: Int!

        """data from the rows affected by the mutation"""
        returning: [contract_token_anti_storage!]!
        }

        """
        on_conflict condition type for table "contract_token_anti_storage"
        """
        input contract_token_anti_storage_on_conflict {
        constraInt: contract_token_anti_storage_constraInt!
        update_columns: [contract_token_anti_storage_update_column!]! = []
        where: contract_token_anti_storage_bool_exp
        }

        """
        Ordering options when selecting data from "contract_token_anti_storage".
        """
        input contract_token_anti_storage_order_by {
        admin: order_by
        allowances: order_by
        burn_address: order_by
        burned_supply: order_by
        id: order_by
        initial_supply: order_by
        ledger: order_by
        metadata: order_by
        reserve: order_by
        token_metadata: order_by
        total_supply: order_by
        }

        """primary key columns input for table: contract_token_anti_storage"""
        input contract_token_anti_storage_pk_columns_input {
        id: Int!
        }

        """
        select columns of table "contract_token_anti_storage"
        """
        enum contract_token_anti_storage_select_column {
        """column name"""
        admin

        """column name"""
        allowances

        """column name"""
        burn_address

        """column name"""
        burned_supply

        """column name"""
        id

        """column name"""
        initial_supply

        """column name"""
        ledger

        """column name"""
        metadata

        """column name"""
        reserve

        """column name"""
        token_metadata

        """column name"""
        total_supply
        }

        """
        input type for updating data in table "contract_token_anti_storage"
        """
        input contract_token_anti_storage_set_input {
        admin: String
        allowances: String
        burn_address: String
        burned_supply: String
        id: Int
        initial_supply: String
        ledger: String
        metadata: String
        reserve: String
        token_metadata: String
        total_supply: String
        }

        """aggregate stddev on columns"""
        type contract_token_anti_storage_stddev_fields {
        id: Float
        }

        """aggregate stddev_pop on columns"""
        type contract_token_anti_storage_stddev_pop_fields {
        id: Float
        }

        """aggregate stddev_samp on columns"""
        type contract_token_anti_storage_stddev_samp_fields {
        id: Float
        }

        """
        Streaming cursor of the table "contract_token_anti_storage"
        """
        input contract_token_anti_storage_stream_cursor_input {
        """Stream column input with initial value"""
        initial_value: contract_token_anti_storage_stream_cursor_value_input!

        """cursor ordering"""
        ordering: cursor_ordering
        }

        """Initial value of the column from where the streaming should start"""
        input contract_token_anti_storage_stream_cursor_value_input {
        admin: String
        allowances: String
        burn_address: String
        burned_supply: String
        id: Int
        initial_supply: String
        ledger: String
        metadata: String
        reserve: String
        token_metadata: String
        total_supply: String
        }

        """aggregate sum on columns"""
        type contract_token_anti_storage_sum_fields {
        id: Int
        }

        """
        update columns of table "contract_token_anti_storage"
        """
        enum contract_token_anti_storage_update_column {
        """column name"""
        admin

        """column name"""
        allowances

        """column name"""
        burn_address

        """column name"""
        burned_supply

        """column name"""
        id

        """column name"""
        initial_supply

        """column name"""
        ledger

        """column name"""
        metadata

        """column name"""
        reserve

        """column name"""
        token_metadata

        """column name"""
        total_supply
        }

        input contract_token_anti_storage_updates {
        """increments the numeric columns with given value of the filtered values"""
        _inc: contract_token_anti_storage_inc_input

        """sets the columns of the filtered rows to the given values"""
        _set: contract_token_anti_storage_set_input

        """filter the rows which have to be updated"""
        where: contract_token_anti_storage_bool_exp!
        }

        """aggregate var_pop on columns"""
        type contract_token_anti_storage_var_pop_fields {
        id: Float
        }

        """aggregate var_samp on columns"""
        type contract_token_anti_storage_var_samp_fields {
        id: Float
        }

        """aggregate variance on columns"""
        type contract_token_anti_storage_variance_fields {
        id: Float
        }

        """
        columns and relationships of "contract_token_smak_operations"
        """
        type contract_token_smak_operations {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        block: String
        counter: Int
        errors: String
        eventscount: Int
        gaslimit: Int
        gasused: Int
        hash: String
        hasInternals: Boolean
        id: Int!
        initiator: String
        level: Int
        nonce: Int
        parameter: String
        sender: String
        sendercodehash: Int
        status: String
        storagefee: Int
        storagelimit: Int
        storageused: Int
        target: String
        targetcodehash: Int
        timestamp: Int
        tokentransferscount: Int
        type: String
        }

        """
        aggregated selection of "contract_token_smak_operations"
        """
        type contract_token_smak_operations_aggregate {
        aggregate: contract_token_smak_operations_aggregate_fields
        nodes: [contract_token_smak_operations!]!
        }

        """
        aggregate fields of "contract_token_smak_operations"
        """
        type contract_token_smak_operations_aggregate_fields {
        avg: contract_token_smak_operations_avg_fields
        count(columns: [contract_token_smak_operations_select_column!], distinct: Boolean): Int!
        max: contract_token_smak_operations_max_fields
        min: contract_token_smak_operations_min_fields
        stddev: contract_token_smak_operations_stddev_fields
        stddev_pop: contract_token_smak_operations_stddev_pop_fields
        stddev_samp: contract_token_smak_operations_stddev_samp_fields
        sum: contract_token_smak_operations_sum_fields
        var_pop: contract_token_smak_operations_var_pop_fields
        var_samp: contract_token_smak_operations_var_samp_fields
        variance: contract_token_smak_operations_variance_fields
        }

        """aggregate avg on columns"""
        type contract_token_smak_operations_avg_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """
        Boolean expression to filter rows from the table "contract_token_smak_operations". All fields are combined with a logical 'AND'.
        """
        input contract_token_smak_operations_bool_exp {
        _and: [contract_token_smak_operations_bool_exp!]
        _not: contract_token_smak_operations_bool_exp
        _or: [contract_token_smak_operations_bool_exp!]
        allocationfee: Int_comparison_exp
        amount: Int_comparison_exp
        bakerfee: Int_comparison_exp
        block: String_comparison_exp
        counter: Int_comparison_exp
        errors: String_comparison_exp
        eventscount: Int_comparison_exp
        gaslimit: Int_comparison_exp
        gasused: Int_comparison_exp
        hash: String_comparison_exp
        hasInternals: Boolean_comparison_exp
        id: Int_comparison_exp
        initiator: String_comparison_exp
        level: Int_comparison_exp
        nonce: Int_comparison_exp
        parameter: String_comparison_exp
        sender: String_comparison_exp
        sendercodehash: Int_comparison_exp
        status: String_comparison_exp
        storagefee: Int_comparison_exp
        storagelimit: Int_comparison_exp
        storageused: Int_comparison_exp
        target: String_comparison_exp
        targetcodehash: Int_comparison_exp
        timestamp: Int_comparison_exp
        tokentransferscount: Int_comparison_exp
        type: String_comparison_exp
        }

        """
        unique or primary key constraInts on table "contract_token_smak_operations"
        """
        enum contract_token_smak_operations_constraInt {
        """
        unique or primary key constraInt on columns "id"
        """
        contract_token_smak_operations_pkey
        }

        """
        input type for incrementing numeric columns in table "contract_token_smak_operations"
        """
        input contract_token_smak_operations_inc_input {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        counter: Int
        eventscount: Int
        gaslimit: Int
        gasused: Int
        id: Int
        level: Int
        nonce: Int
        sendercodehash: Int
        storagefee: Int
        storagelimit: Int
        storageused: Int
        targetcodehash: Int
        tokentransferscount: Int
        }

        """
        input type for inserting data Into table "contract_token_smak_operations"
        """
        input contract_token_smak_operations_insert_input {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        block: String
        counter: Int
        errors: String
        eventscount: Int
        gaslimit: Int
        gasused: Int
        hash: String
        hasInternals: Boolean
        id: Int
        initiator: String
        level: Int
        nonce: Int
        parameter: String
        sender: String
        sendercodehash: Int
        status: String
        storagefee: Int
        storagelimit: Int
        storageused: Int
        target: String
        targetcodehash: Int
        timestamp: Int
        tokentransferscount: Int
        type: String
        }

        """aggregate max on columns"""
        type contract_token_smak_operations_max_fields {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        block: String
        counter: Int
        errors: String
        eventscount: Int
        gaslimit: Int
        gasused: Int
        hash: String
        id: Int
        initiator: String
        level: Int
        nonce: Int
        parameter: String
        sender: String
        sendercodehash: Int
        status: String
        storagefee: Int
        storagelimit: Int
        storageused: Int
        target: String
        targetcodehash: Int
        timestamp: Int
        tokentransferscount: Int
        type: String
        }

        """aggregate min on columns"""
        type contract_token_smak_operations_min_fields {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        block: String
        counter: Int
        errors: String
        eventscount: Int
        gaslimit: Int
        gasused: Int
        hash: String
        id: Int
        initiator: String
        level: Int
        nonce: Int
        parameter: String
        sender: String
        sendercodehash: Int
        status: String
        storagefee: Int
        storagelimit: Int
        storageused: Int
        target: String
        targetcodehash: Int
        timestamp: Int
        tokentransferscount: Int
        type: String
        }

        """
        response of any mutation on the table "contract_token_smak_operations"
        """
        type contract_token_smak_operations_mutation_response {
        """number of rows affected by the mutation"""
        affected_rows: Int!

        """data from the rows affected by the mutation"""
        returning: [contract_token_smak_operations!]!
        }

        """
        on_conflict condition type for table "contract_token_smak_operations"
        """
        input contract_token_smak_operations_on_conflict {
        constraInt: contract_token_smak_operations_constraInt!
        update_columns: [contract_token_smak_operations_update_column!]! = []
        where: contract_token_smak_operations_bool_exp
        }

        """
        Ordering options when selecting data from "contract_token_smak_operations".
        """
        input contract_token_smak_operations_order_by {
        allocationfee: order_by
        amount: order_by
        bakerfee: order_by
        block: order_by
        counter: order_by
        errors: order_by
        eventscount: order_by
        gaslimit: order_by
        gasused: order_by
        hash: order_by
        hasInternals: order_by
        id: order_by
        initiator: order_by
        level: order_by
        nonce: order_by
        parameter: order_by
        sender: order_by
        sendercodehash: order_by
        status: order_by
        storagefee: order_by
        storagelimit: order_by
        storageused: order_by
        target: order_by
        targetcodehash: order_by
        timestamp: order_by
        tokentransferscount: order_by
        type: order_by
        }

        """primary key columns input for table: contract_token_smak_operations"""
        input contract_token_smak_operations_pk_columns_input {
        id: Int!
        }

        """
        select columns of table "contract_token_smak_operations"
        """
        enum contract_token_smak_operations_select_column {
        """column name"""
        allocationfee

        """column name"""
        amount

        """column name"""
        bakerfee

        """column name"""
        block

        """column name"""
        counter

        """column name"""
        errors

        """column name"""
        eventscount

        """column name"""
        gaslimit

        """column name"""
        gasused

        """column name"""
        hash

        """column name"""
        hasInternals

        """column name"""
        id

        """column name"""
        initiator

        """column name"""
        level

        """column name"""
        nonce

        """column name"""
        parameter

        """column name"""
        sender

        """column name"""
        sendercodehash

        """column name"""
        status

        """column name"""
        storagefee

        """column name"""
        storagelimit

        """column name"""
        storageused

        """column name"""
        target

        """column name"""
        targetcodehash

        """column name"""
        timestamp

        """column name"""
        tokentransferscount

        """column name"""
        type
        }

        """
        input type for updating data in table "contract_token_smak_operations"
        """
        input contract_token_smak_operations_set_input {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        block: String
        counter: Int
        errors: String
        eventscount: Int
        gaslimit: Int
        gasused: Int
        hash: String
        hasInternals: Boolean
        id: Int
        initiator: String
        level: Int
        nonce: Int
        parameter: String
        sender: String
        sendercodehash: Int
        status: String
        storagefee: Int
        storagelimit: Int
        storageused: Int
        target: String
        targetcodehash: Int
        timestamp: Int
        tokentransferscount: Int
        type: String
        }

        """aggregate stddev on columns"""
        type contract_token_smak_operations_stddev_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """aggregate stddev_pop on columns"""
        type contract_token_smak_operations_stddev_pop_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """aggregate stddev_samp on columns"""
        type contract_token_smak_operations_stddev_samp_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """
        Streaming cursor of the table "contract_token_smak_operations"
        """
        input contract_token_smak_operations_stream_cursor_input {
        """Stream column input with initial value"""
        initial_value: contract_token_smak_operations_stream_cursor_value_input!

        """cursor ordering"""
        ordering: cursor_ordering
        }

        """Initial value of the column from where the streaming should start"""
        input contract_token_smak_operations_stream_cursor_value_input {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        block: String
        counter: Int
        errors: String
        eventscount: Int
        gaslimit: Int
        gasused: Int
        hash: String
        hasInternals: Boolean
        id: Int
        initiator: String
        level: Int
        nonce: Int
        parameter: String
        sender: String
        sendercodehash: Int
        status: String
        storagefee: Int
        storagelimit: Int
        storageused: Int
        target: String
        targetcodehash: Int
        timestamp: Int
        tokentransferscount: Int
        type: String
        }

        """aggregate sum on columns"""
        type contract_token_smak_operations_sum_fields {
        allocationfee: Int
        amount: Int
        bakerfee: Int
        counter: Int
        eventscount: Int
        gaslimit: Int
        gasused: Int
        id: Int
        level: Int
        nonce: Int
        sendercodehash: Int
        storagefee: Int
        storagelimit: Int
        storageused: Int
        targetcodehash: Int
        tokentransferscount: Int
        }

        """
        update columns of table "contract_token_smak_operations"
        """
        enum contract_token_smak_operations_update_column {
        """column name"""
        allocationfee

        """column name"""
        amount

        """column name"""
        bakerfee

        """column name"""
        block

        """column name"""
        counter

        """column name"""
        errors

        """column name"""
        eventscount

        """column name"""
        gaslimit

        """column name"""
        gasused

        """column name"""
        hash

        """column name"""
        hasInternals

        """column name"""
        id

        """column name"""
        initiator

        """column name"""
        level

        """column name"""
        nonce

        """column name"""
        parameter

        """column name"""
        sender

        """column name"""
        sendercodehash

        """column name"""
        status

        """column name"""
        storagefee

        """column name"""
        storagelimit

        """column name"""
        storageused

        """column name"""
        target

        """column name"""
        targetcodehash

        """column name"""
        timestamp

        """column name"""
        tokentransferscount

        """column name"""
        type
        }

        input contract_token_smak_operations_updates {
        """increments the numeric columns with given value of the filtered values"""
        _inc: contract_token_smak_operations_inc_input

        """sets the columns of the filtered rows to the given values"""
        _set: contract_token_smak_operations_set_input

        """filter the rows which have to be updated"""
        where: contract_token_smak_operations_bool_exp!
        }

        """aggregate var_pop on columns"""
        type contract_token_smak_operations_var_pop_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """aggregate var_samp on columns"""
        type contract_token_smak_operations_var_samp_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """aggregate variance on columns"""
        type contract_token_smak_operations_variance_fields {
        allocationfee: Float
        amount: Float
        bakerfee: Float
        counter: Float
        eventscount: Float
        gaslimit: Float
        gasused: Float
        id: Float
        level: Float
        nonce: Float
        sendercodehash: Float
        storagefee: Float
        storagelimit: Float
        storageused: Float
        targetcodehash: Float
        tokentransferscount: Float
        }

        """
        columns and relationships of "contract_token_smak_storage"
        """
        type contract_token_smak_storage {
        administrator: String
        balances: String
        freezer: String
        frozen_accounts: String
        id: Int!
        metadata: String
        token_metadata: String
        totalsupply: String
        }

        """
        aggregated selection of "contract_token_smak_storage"
        """
        type contract_token_smak_storage_aggregate {
        aggregate: contract_token_smak_storage_aggregate_fields
        nodes: [contract_token_smak_storage!]!
        }

        """
        aggregate fields of "contract_token_smak_storage"
        """
        type contract_token_smak_storage_aggregate_fields {
        avg: contract_token_smak_storage_avg_fields
        count(columns: [contract_token_smak_storage_select_column!], distinct: Boolean): Int!
        max: contract_token_smak_storage_max_fields
        min: contract_token_smak_storage_min_fields
        stddev: contract_token_smak_storage_stddev_fields
        stddev_pop: contract_token_smak_storage_stddev_pop_fields
        stddev_samp: contract_token_smak_storage_stddev_samp_fields
        sum: contract_token_smak_storage_sum_fields
        var_pop: contract_token_smak_storage_var_pop_fields
        var_samp: contract_token_smak_storage_var_samp_fields
        variance: contract_token_smak_storage_variance_fields
        }

        """aggregate avg on columns"""
        type contract_token_smak_storage_avg_fields {
        id: Float
        }

        """
        Boolean expression to filter rows from the table "contract_token_smak_storage". All fields are combined with a logical 'AND'.
        """
        input contract_token_smak_storage_bool_exp {
        _and: [contract_token_smak_storage_bool_exp!]
        _not: contract_token_smak_storage_bool_exp
        _or: [contract_token_smak_storage_bool_exp!]
        administrator: String_comparison_exp
        balances: String_comparison_exp
        freezer: String_comparison_exp
        frozen_accounts: String_comparison_exp
        id: Int_comparison_exp
        metadata: String_comparison_exp
        token_metadata: String_comparison_exp
        totalsupply: String_comparison_exp
        }

        """
        unique or primary key constraInts on table "contract_token_smak_storage"
        """
        enum contract_token_smak_storage_constraInt {
        """
        unique or primary key constraInt on columns "id"
        """
        contract_token_smak_storage_pkey
        }

        """
        input type for incrementing numeric columns in table "contract_token_smak_storage"
        """
        input contract_token_smak_storage_inc_input {
        id: Int
        }

        """
        input type for inserting data Into table "contract_token_smak_storage"
        """
        input contract_token_smak_storage_insert_input {
        administrator: String
        balances: String
        freezer: String
        frozen_accounts: String
        id: Int
        metadata: String
        token_metadata: String
        totalsupply: String
        }

        """aggregate max on columns"""
        type contract_token_smak_storage_max_fields {
        administrator: String
        balances: String
        freezer: String
        frozen_accounts: String
        id: Int
        metadata: String
        token_metadata: String
        totalsupply: String
        }

        """aggregate min on columns"""
        type contract_token_smak_storage_min_fields {
        administrator: String
        balances: String
        freezer: String
        frozen_accounts: String
        id: Int
        metadata: String
        token_metadata: String
        totalsupply: String
        }

        """
        response of any mutation on the table "contract_token_smak_storage"
        """
        type contract_token_smak_storage_mutation_response {
        """number of rows affected by the mutation"""
        affected_rows: Int!

        """data from the rows affected by the mutation"""
        returning: [contract_token_smak_storage!]!
        }

        """
        on_conflict condition type for table "contract_token_smak_storage"
        """
        input contract_token_smak_storage_on_conflict {
        constraInt: contract_token_smak_storage_constraInt!
        update_columns: [contract_token_smak_storage_update_column!]! = []
        where: contract_token_smak_storage_bool_exp
        }

        """
        Ordering options when selecting data from "contract_token_smak_storage".
        """
        input contract_token_smak_storage_order_by {
        administrator: order_by
        balances: order_by
        freezer: order_by
        frozen_accounts: order_by
        id: order_by
        metadata: order_by
        token_metadata: order_by
        totalsupply: order_by
        }

        """primary key columns input for table: contract_token_smak_storage"""
        input contract_token_smak_storage_pk_columns_input {
        id: Int!
        }

        """
        select columns of table "contract_token_smak_storage"
        """
        enum contract_token_smak_storage_select_column {
        """column name"""
        administrator

        """column name"""
        balances

        """column name"""
        freezer

        """column name"""
        frozen_accounts

        """column name"""
        id

        """column name"""
        metadata

        """column name"""
        token_metadata

        """column name"""
        totalsupply
        }

        """
        input type for updating data in table "contract_token_smak_storage"
        """
        input contract_token_smak_storage_set_input {
        administrator: String
        balances: String
        freezer: String
        frozen_accounts: String
        id: Int
        metadata: String
        token_metadata: String
        totalsupply: String
        }

        """aggregate stddev on columns"""
        type contract_token_smak_storage_stddev_fields {
        id: Float
        }

        """aggregate stddev_pop on columns"""
        type contract_token_smak_storage_stddev_pop_fields {
        id: Float
        }

        """aggregate stddev_samp on columns"""
        type contract_token_smak_storage_stddev_samp_fields {
        id: Float
        }

        """
        Streaming cursor of the table "contract_token_smak_storage"
        """
        input contract_token_smak_storage_stream_cursor_input {
        """Stream column input with initial value"""
        initial_value: contract_token_smak_storage_stream_cursor_value_input!

        """cursor ordering"""
        ordering: cursor_ordering
        }

        """Initial value of the column from where the streaming should start"""
        input contract_token_smak_storage_stream_cursor_value_input {
        administrator: String
        balances: String
        freezer: String
        frozen_accounts: String
        id: Int
        metadata: String
        token_metadata: String
        totalsupply: String
        }

        """aggregate sum on columns"""
        type contract_token_smak_storage_sum_fields {
        id: Int
        }

        """
        update columns of table "contract_token_smak_storage"
        """
        enum contract_token_smak_storage_update_column {
        """column name"""
        administrator

        """column name"""
        balances

        """column name"""
        freezer

        """column name"""
        frozen_accounts

        """column name"""
        id

        """column name"""
        metadata

        """column name"""
        token_metadata

        """column name"""
        totalsupply
        }

        input contract_token_smak_storage_updates {
        """increments the numeric columns with given value of the filtered values"""
        _inc: contract_token_smak_storage_inc_input

        """sets the columns of the filtered rows to the given values"""
        _set: contract_token_smak_storage_set_input

        """filter the rows which have to be updated"""
        where: contract_token_smak_storage_bool_exp!
        }

        """aggregate var_pop on columns"""
        type contract_token_smak_storage_var_pop_fields {
        id: Float
        }

        """aggregate var_samp on columns"""
        type contract_token_smak_storage_var_samp_fields {
        id: Float
        }

        """aggregate variance on columns"""
        type contract_token_smak_storage_variance_fields {
        id: Float
        }

        """ordering argument of a cursor"""
        enum cursor_ordering {
        """ascending ordering of the cursor"""
        ASC

        """descending ordering of the cursor"""
        DESC
        }

        """
        columns and relationships of "indexer"
        """
        type indexer {
        circulatingsupply: Int
        id: Int!
        level: Int
        timestamp: Int
        totalactivated: Int
        totalbanished: Int
        totalbootstrapped: Int
        totalburned: Int
        totalcommitments: Int
        totalcreated: Int
        totalfrozen: Int
        totalrollupbonds: Int
        totalsmartrollupbonds: Int
        totalsupply: Int
        totalvested: Int
        }

        """
        aggregated selection of "indexer"
        """
        type indexer_aggregate {
        aggregate: indexer_aggregate_fields
        nodes: [indexer!]!
        }

        """
        aggregate fields of "indexer"
        """
        type indexer_aggregate_fields {
        avg: indexer_avg_fields
        count(columns: [indexer_select_column!], distinct: Boolean): Int!
        max: indexer_max_fields
        min: indexer_min_fields
        stddev: indexer_stddev_fields
        stddev_pop: indexer_stddev_pop_fields
        stddev_samp: indexer_stddev_samp_fields
        sum: indexer_sum_fields
        var_pop: indexer_var_pop_fields
        var_samp: indexer_var_samp_fields
        variance: indexer_variance_fields
        }

        """aggregate avg on columns"""
        type indexer_avg_fields {
        circulatingsupply: Float
        id: Float
        level: Float
        totalactivated: Float
        totalbanished: Float
        totalbootstrapped: Float
        totalburned: Float
        totalcommitments: Float
        totalcreated: Float
        totalfrozen: Float
        totalrollupbonds: Float
        totalsmartrollupbonds: Float
        totalsupply: Float
        totalvested: Float
        }

        """
        Boolean expression to filter rows from the table "indexer". All fields are combined with a logical 'AND'.
        """
        input indexer_bool_exp {
        _and: [indexer_bool_exp!]
        _not: indexer_bool_exp
        _or: [indexer_bool_exp!]
        circulatingsupply: Int_comparison_exp
        id: Int_comparison_exp
        level: Int_comparison_exp
        timestamp: Int_comparison_exp
        totalactivated: Int_comparison_exp
        totalbanished: Int_comparison_exp
        totalbootstrapped: Int_comparison_exp
        totalburned: Int_comparison_exp
        totalcommitments: Int_comparison_exp
        totalcreated: Int_comparison_exp
        totalfrozen: Int_comparison_exp
        totalrollupbonds: Int_comparison_exp
        totalsmartrollupbonds: Int_comparison_exp
        totalsupply: Int_comparison_exp
        totalvested: Int_comparison_exp
        }

        """
        unique or primary key constraInts on table "indexer"
        """
        enum indexer_constraInt {
        """
        unique or primary key constraInt on columns "id"
        """
        indexer_pkey
        }

        """
        input type for incrementing numeric columns in table "indexer"
        """
        input indexer_inc_input {
        circulatingsupply: Int
        id: Int
        level: Int
        totalactivated: Int
        totalbanished: Int
        totalbootstrapped: Int
        totalburned: Int
        totalcommitments: Int
        totalcreated: Int
        totalfrozen: Int
        totalrollupbonds: Int
        totalsmartrollupbonds: Int
        totalsupply: Int
        totalvested: Int
        }

        """
        input type for inserting data Into table "indexer"
        """
        input indexer_insert_input {
        circulatingsupply: Int
        id: Int
        level: Int
        timestamp: Int
        totalactivated: Int
        totalbanished: Int
        totalbootstrapped: Int
        totalburned: Int
        totalcommitments: Int
        totalcreated: Int
        totalfrozen: Int
        totalrollupbonds: Int
        totalsmartrollupbonds: Int
        totalsupply: Int
        totalvested: Int
        }

        """aggregate max on columns"""
        type indexer_max_fields {
        circulatingsupply: Int
        id: Int
        level: Int
        timestamp: Int
        totalactivated: Int
        totalbanished: Int
        totalbootstrapped: Int
        totalburned: Int
        totalcommitments: Int
        totalcreated: Int
        totalfrozen: Int
        totalrollupbonds: Int
        totalsmartrollupbonds: Int
        totalsupply: Int
        totalvested: Int
        }

        """aggregate min on columns"""
        type indexer_min_fields {
        circulatingsupply: Int
        id: Int
        level: Int
        timestamp: Int
        totalactivated: Int
        totalbanished: Int
        totalbootstrapped: Int
        totalburned: Int
        totalcommitments: Int
        totalcreated: Int
        totalfrozen: Int
        totalrollupbonds: Int
        totalsmartrollupbonds: Int
        totalsupply: Int
        totalvested: Int
        }

        """
        response of any mutation on the table "indexer"
        """
        type indexer_mutation_response {
        """number of rows affected by the mutation"""
        affected_rows: Int!

        """data from the rows affected by the mutation"""
        returning: [indexer!]!
        }

        """
        on_conflict condition type for table "indexer"
        """
        input indexer_on_conflict {
        constraInt: indexer_constraInt!
        update_columns: [indexer_update_column!]! = []
        where: indexer_bool_exp
        }

        """Ordering options when selecting data from "indexer"."""
        input indexer_order_by {
        circulatingsupply: order_by
        id: order_by
        level: order_by
        timestamp: order_by
        totalactivated: order_by
        totalbanished: order_by
        totalbootstrapped: order_by
        totalburned: order_by
        totalcommitments: order_by
        totalcreated: order_by
        totalfrozen: order_by
        totalrollupbonds: order_by
        totalsmartrollupbonds: order_by
        totalsupply: order_by
        totalvested: order_by
        }

        """primary key columns input for table: indexer"""
        input indexer_pk_columns_input {
        id: Int!
        }

        """
        select columns of table "indexer"
        """
        enum indexer_select_column {
        """column name"""
        circulatingsupply

        """column name"""
        id

        """column name"""
        level

        """column name"""
        timestamp

        """column name"""
        totalactivated

        """column name"""
        totalbanished

        """column name"""
        totalbootstrapped

        """column name"""
        totalburned

        """column name"""
        totalcommitments

        """column name"""
        totalcreated

        """column name"""
        totalfrozen

        """column name"""
        totalrollupbonds

        """column name"""
        totalsmartrollupbonds

        """column name"""
        totalsupply

        """column name"""
        totalvested
        }

        """
        input type for updating data in table "indexer"
        """
        input indexer_set_input {
        circulatingsupply: Int
        id: Int
        level: Int
        timestamp: Int
        totalactivated: Int
        totalbanished: Int
        totalbootstrapped: Int
        totalburned: Int
        totalcommitments: Int
        totalcreated: Int
        totalfrozen: Int
        totalrollupbonds: Int
        totalsmartrollupbonds: Int
        totalsupply: Int
        totalvested: Int
        }

        """aggregate stddev on columns"""
        type indexer_stddev_fields {
        circulatingsupply: Float
        id: Float
        level: Float
        totalactivated: Float
        totalbanished: Float
        totalbootstrapped: Float
        totalburned: Float
        totalcommitments: Float
        totalcreated: Float
        totalfrozen: Float
        totalrollupbonds: Float
        totalsmartrollupbonds: Float
        totalsupply: Float
        totalvested: Float
        }

        """aggregate stddev_pop on columns"""
        type indexer_stddev_pop_fields {
        circulatingsupply: Float
        id: Float
        level: Float
        totalactivated: Float
        totalbanished: Float
        totalbootstrapped: Float
        totalburned: Float
        totalcommitments: Float
        totalcreated: Float
        totalfrozen: Float
        totalrollupbonds: Float
        totalsmartrollupbonds: Float
        totalsupply: Float
        totalvested: Float
        }

        """aggregate stddev_samp on columns"""
        type indexer_stddev_samp_fields {
        circulatingsupply: Float
        id: Float
        level: Float
        totalactivated: Float
        totalbanished: Float
        totalbootstrapped: Float
        totalburned: Float
        totalcommitments: Float
        totalcreated: Float
        totalfrozen: Float
        totalrollupbonds: Float
        totalsmartrollupbonds: Float
        totalsupply: Float
        totalvested: Float
        }

        """
        Streaming cursor of the table "indexer"
        """
        input indexer_stream_cursor_input {
        """Stream column input with initial value"""
        initial_value: indexer_stream_cursor_value_input!

        """cursor ordering"""
        ordering: cursor_ordering
        }

        """Initial value of the column from where the streaming should start"""
        input indexer_stream_cursor_value_input {
        circulatingsupply: Int
        id: Int
        level: Int
        timestamp: Int
        totalactivated: Int
        totalbanished: Int
        totalbootstrapped: Int
        totalburned: Int
        totalcommitments: Int
        totalcreated: Int
        totalfrozen: Int
        totalrollupbonds: Int
        totalsmartrollupbonds: Int
        totalsupply: Int
        totalvested: Int
        }

        """aggregate sum on columns"""
        type indexer_sum_fields {
        circulatingsupply: Int
        id: Int
        level: Int
        totalactivated: Int
        totalbanished: Int
        totalbootstrapped: Int
        totalburned: Int
        totalcommitments: Int
        totalcreated: Int
        totalfrozen: Int
        totalrollupbonds: Int
        totalsmartrollupbonds: Int
        totalsupply: Int
        totalvested: Int
        }

        """
        update columns of table "indexer"
        """
        enum indexer_update_column {
        """column name"""
        circulatingsupply

        """column name"""
        id

        """column name"""
        level

        """column name"""
        timestamp

        """column name"""
        totalactivated

        """column name"""
        totalbanished

        """column name"""
        totalbootstrapped

        """column name"""
        totalburned

        """column name"""
        totalcommitments

        """column name"""
        totalcreated

        """column name"""
        totalfrozen

        """column name"""
        totalrollupbonds

        """column name"""
        totalsmartrollupbonds

        """column name"""
        totalsupply

        """column name"""
        totalvested
        }

        input indexer_updates {
        """increments the numeric columns with given value of the filtered values"""
        _inc: indexer_inc_input

        """sets the columns of the filtered rows to the given values"""
        _set: indexer_set_input

        """filter the rows which have to be updated"""
        where: indexer_bool_exp!
        }

        """aggregate var_pop on columns"""
        type indexer_var_pop_fields {
        circulatingsupply: Float
        id: Float
        level: Float
        totalactivated: Float
        totalbanished: Float
        totalbootstrapped: Float
        totalburned: Float
        totalcommitments: Float
        totalcreated: Float
        totalfrozen: Float
        totalrollupbonds: Float
        totalsmartrollupbonds: Float
        totalsupply: Float
        totalvested: Float
        }

        """aggregate var_samp on columns"""
        type indexer_var_samp_fields {
        circulatingsupply: Float
        id: Float
        level: Float
        totalactivated: Float
        totalbanished: Float
        totalbootstrapped: Float
        totalburned: Float
        totalcommitments: Float
        totalcreated: Float
        totalfrozen: Float
        totalrollupbonds: Float
        totalsmartrollupbonds: Float
        totalsupply: Float
        totalvested: Float
        }

        """aggregate variance on columns"""
        type indexer_variance_fields {
        circulatingsupply: Float
        id: Float
        level: Float
        totalactivated: Float
        totalbanished: Float
        totalbootstrapped: Float
        totalburned: Float
        totalcommitments: Float
        totalcreated: Float
        totalfrozen: Float
        totalrollupbonds: Float
        totalsmartrollupbonds: Float
        totalsupply: Float
        totalvested: Float
        }

        """mutation root"""
        type mutation_root {
        """
        delete data from the table: "contract_dex_operations"
        """
        delete_contract_dex_operations(
            """filter the rows which have to be deleted"""
            where: contract_dex_operations_bool_exp!
        ): contract_dex_operations_mutation_response

        """
        delete single row from the table: "contract_dex_operations"
        """
        delete_contract_dex_operations_by_pk(id: Int!): contract_dex_operations

        """
        delete data from the table: "contract_dex_storage"
        """
        delete_contract_dex_storage(
            """filter the rows which have to be deleted"""
            where: contract_dex_storage_bool_exp!
        ): contract_dex_storage_mutation_response

        """
        delete single row from the table: "contract_dex_storage"
        """
        delete_contract_dex_storage_by_pk(id: Int!): contract_dex_storage

        """
        delete data from the table: "contract_factory_doga_operations"
        """
        delete_contract_factory_doga_operations(
            """filter the rows which have to be deleted"""
            where: contract_factory_doga_operations_bool_exp!
        ): contract_factory_doga_operations_mutation_response

        """
        delete single row from the table: "contract_factory_doga_operations"
        """
        delete_contract_factory_doga_operations_by_pk(id: Int!): contract_factory_doga_operations

        """
        delete data from the table: "contract_factory_doga_storage"
        """
        delete_contract_factory_doga_storage(
            """filter the rows which have to be deleted"""
            where: contract_factory_doga_storage_bool_exp!
        ): contract_factory_doga_storage_mutation_response

        """
        delete single row from the table: "contract_factory_doga_storage"
        """
        delete_contract_factory_doga_storage_by_pk(id: Int!): contract_factory_doga_storage

        """
        delete data from the table: "contract_factory_fa12_operations"
        """
        delete_contract_factory_fa12_operations(
            """filter the rows which have to be deleted"""
            where: contract_factory_fa12_operations_bool_exp!
        ): contract_factory_fa12_operations_mutation_response

        """
        delete single row from the table: "contract_factory_fa12_operations"
        """
        delete_contract_factory_fa12_operations_by_pk(id: Int!): contract_factory_fa12_operations

        """
        delete data from the table: "contract_factory_fa12_storage"
        """
        delete_contract_factory_fa12_storage(
            """filter the rows which have to be deleted"""
            where: contract_factory_fa12_storage_bool_exp!
        ): contract_factory_fa12_storage_mutation_response

        """
        delete single row from the table: "contract_factory_fa12_storage"
        """
        delete_contract_factory_fa12_storage_by_pk(id: Int!): contract_factory_fa12_storage

        """
        delete data from the table: "contract_factory_fa2_operations"
        """
        delete_contract_factory_fa2_operations(
            """filter the rows which have to be deleted"""
            where: contract_factory_fa2_operations_bool_exp!
        ): contract_factory_fa2_operations_mutation_response

        """
        delete single row from the table: "contract_factory_fa2_operations"
        """
        delete_contract_factory_fa2_operations_by_pk(id: Int!): contract_factory_fa2_operations

        """
        delete data from the table: "contract_factory_fa2_storage"
        """
        delete_contract_factory_fa2_storage(
            """filter the rows which have to be deleted"""
            where: contract_factory_fa2_storage_bool_exp!
        ): contract_factory_fa2_storage_mutation_response

        """
        delete single row from the table: "contract_factory_fa2_storage"
        """
        delete_contract_factory_fa2_storage_by_pk(id: Int!): contract_factory_fa2_storage

        """
        delete data from the table: "contract_farms_v1_operations"
        """
        delete_contract_farms_v1_operations(
            """filter the rows which have to be deleted"""
            where: contract_farms_v1_operations_bool_exp!
        ): contract_farms_v1_operations_mutation_response

        """
        delete single row from the table: "contract_farms_v1_operations"
        """
        delete_contract_farms_v1_operations_by_pk(id: Int!): contract_farms_v1_operations

        """
        delete data from the table: "contract_farms_v1_storage"
        """
        delete_contract_farms_v1_storage(
            """filter the rows which have to be deleted"""
            where: contract_farms_v1_storage_bool_exp!
        ): contract_farms_v1_storage_mutation_response

        """
        delete single row from the table: "contract_farms_v1_storage"
        """
        delete_contract_farms_v1_storage_by_pk(id: Int!): contract_farms_v1_storage

        """
        delete data from the table: "contract_farms_v2_allfarms"
        """
        delete_contract_farms_v2_allfarms(
            """filter the rows which have to be deleted"""
            where: contract_farms_v2_allfarms_bool_exp!
        ): contract_farms_v2_allfarms_mutation_response

        """
        delete single row from the table: "contract_farms_v2_allfarms"
        """
        delete_contract_farms_v2_allfarms_by_pk(id: Int!): contract_farms_v2_allfarms

        """
        delete data from the table: "contract_farms_v2_operations"
        """
        delete_contract_farms_v2_operations(
            """filter the rows which have to be deleted"""
            where: contract_farms_v2_operations_bool_exp!
        ): contract_farms_v2_operations_mutation_response

        """
        delete single row from the table: "contract_farms_v2_operations"
        """
        delete_contract_farms_v2_operations_by_pk(id: Int!): contract_farms_v2_operations

        """
        delete data from the table: "contract_farms_v2_storage"
        """
        delete_contract_farms_v2_storage(
            """filter the rows which have to be deleted"""
            where: contract_farms_v2_storage_bool_exp!
        ): contract_farms_v2_storage_mutation_response

        """
        delete single row from the table: "contract_farms_v2_storage"
        """
        delete_contract_farms_v2_storage_by_pk(id: Int!): contract_farms_v2_storage

        """
        delete data from the table: "contract_staking_smak_operations"
        """
        delete_contract_staking_smak_operations(
            """filter the rows which have to be deleted"""
            where: contract_staking_smak_operations_bool_exp!
        ): contract_staking_smak_operations_mutation_response

        """
        delete single row from the table: "contract_staking_smak_operations"
        """
        delete_contract_staking_smak_operations_by_pk(id: Int!): contract_staking_smak_operations

        """
        delete data from the table: "contract_staking_smak_storage"
        """
        delete_contract_staking_smak_storage(
            """filter the rows which have to be deleted"""
            where: contract_staking_smak_storage_bool_exp!
        ): contract_staking_smak_storage_mutation_response

        """
        delete single row from the table: "contract_staking_smak_storage"
        """
        delete_contract_staking_smak_storage_by_pk(id: Int!): contract_staking_smak_storage

        """
        delete data from the table: "contract_token_anti_operations"
        """
        delete_contract_token_anti_operations(
            """filter the rows which have to be deleted"""
            where: contract_token_anti_operations_bool_exp!
        ): contract_token_anti_operations_mutation_response

        """
        delete single row from the table: "contract_token_anti_operations"
        """
        delete_contract_token_anti_operations_by_pk(id: Int!): contract_token_anti_operations

        """
        delete data from the table: "contract_token_anti_storage"
        """
        delete_contract_token_anti_storage(
            """filter the rows which have to be deleted"""
            where: contract_token_anti_storage_bool_exp!
        ): contract_token_anti_storage_mutation_response

        """
        delete single row from the table: "contract_token_anti_storage"
        """
        delete_contract_token_anti_storage_by_pk(id: Int!): contract_token_anti_storage

        """
        delete data from the table: "contract_token_smak_operations"
        """
        delete_contract_token_smak_operations(
            """filter the rows which have to be deleted"""
            where: contract_token_smak_operations_bool_exp!
        ): contract_token_smak_operations_mutation_response

        """
        delete single row from the table: "contract_token_smak_operations"
        """
        delete_contract_token_smak_operations_by_pk(id: Int!): contract_token_smak_operations

        """
        delete data from the table: "contract_token_smak_storage"
        """
        delete_contract_token_smak_storage(
            """filter the rows which have to be deleted"""
            where: contract_token_smak_storage_bool_exp!
        ): contract_token_smak_storage_mutation_response

        """
        delete single row from the table: "contract_token_smak_storage"
        """
        delete_contract_token_smak_storage_by_pk(id: Int!): contract_token_smak_storage

        """
        delete data from the table: "indexer"
        """
        delete_indexer(
            """filter the rows which have to be deleted"""
            where: indexer_bool_exp!
        ): indexer_mutation_response

        """
        delete single row from the table: "indexer"
        """
        delete_indexer_by_pk(id: Int!): indexer

        """
        insert data Into the table: "contract_dex_operations"
        """
        insert_contract_dex_operations(
            """the rows to be inserted"""
            objects: [contract_dex_operations_insert_input!]!

            """upsert condition"""
            on_conflict: contract_dex_operations_on_conflict
        ): contract_dex_operations_mutation_response

        """
        insert a single row Into the table: "contract_dex_operations"
        """
        insert_contract_dex_operations_one(
            """the row to be inserted"""
            object: contract_dex_operations_insert_input!

            """upsert condition"""
            on_conflict: contract_dex_operations_on_conflict
        ): contract_dex_operations

        """
        insert data Into the table: "contract_dex_storage"
        """
        insert_contract_dex_storage(
            """the rows to be inserted"""
            objects: [contract_dex_storage_insert_input!]!

            """upsert condition"""
            on_conflict: contract_dex_storage_on_conflict
        ): contract_dex_storage_mutation_response

        """
        insert a single row Into the table: "contract_dex_storage"
        """
        insert_contract_dex_storage_one(
            """the row to be inserted"""
            object: contract_dex_storage_insert_input!

            """upsert condition"""
            on_conflict: contract_dex_storage_on_conflict
        ): contract_dex_storage

        """
        insert data Into the table: "contract_factory_doga_operations"
        """
        insert_contract_factory_doga_operations(
            """the rows to be inserted"""
            objects: [contract_factory_doga_operations_insert_input!]!

            """upsert condition"""
            on_conflict: contract_factory_doga_operations_on_conflict
        ): contract_factory_doga_operations_mutation_response

        """
        insert a single row Into the table: "contract_factory_doga_operations"
        """
        insert_contract_factory_doga_operations_one(
            """the row to be inserted"""
            object: contract_factory_doga_operations_insert_input!

            """upsert condition"""
            on_conflict: contract_factory_doga_operations_on_conflict
        ): contract_factory_doga_operations

        """
        insert data Into the table: "contract_factory_doga_storage"
        """
        insert_contract_factory_doga_storage(
            """the rows to be inserted"""
            objects: [contract_factory_doga_storage_insert_input!]!

            """upsert condition"""
            on_conflict: contract_factory_doga_storage_on_conflict
        ): contract_factory_doga_storage_mutation_response

        """
        insert a single row Into the table: "contract_factory_doga_storage"
        """
        insert_contract_factory_doga_storage_one(
            """the row to be inserted"""
            object: contract_factory_doga_storage_insert_input!

            """upsert condition"""
            on_conflict: contract_factory_doga_storage_on_conflict
        ): contract_factory_doga_storage

        """
        insert data Into the table: "contract_factory_fa12_operations"
        """
        insert_contract_factory_fa12_operations(
            """the rows to be inserted"""
            objects: [contract_factory_fa12_operations_insert_input!]!

            """upsert condition"""
            on_conflict: contract_factory_fa12_operations_on_conflict
        ): contract_factory_fa12_operations_mutation_response

        """
        insert a single row Into the table: "contract_factory_fa12_operations"
        """
        insert_contract_factory_fa12_operations_one(
            """the row to be inserted"""
            object: contract_factory_fa12_operations_insert_input!

            """upsert condition"""
            on_conflict: contract_factory_fa12_operations_on_conflict
        ): contract_factory_fa12_operations

        """
        insert data Into the table: "contract_factory_fa12_storage"
        """
        insert_contract_factory_fa12_storage(
            """the rows to be inserted"""
            objects: [contract_factory_fa12_storage_insert_input!]!

            """upsert condition"""
            on_conflict: contract_factory_fa12_storage_on_conflict
        ): contract_factory_fa12_storage_mutation_response

        """
        insert a single row Into the table: "contract_factory_fa12_storage"
        """
        insert_contract_factory_fa12_storage_one(
            """the row to be inserted"""
            object: contract_factory_fa12_storage_insert_input!

            """upsert condition"""
            on_conflict: contract_factory_fa12_storage_on_conflict
        ): contract_factory_fa12_storage

        """
        insert data Into the table: "contract_factory_fa2_operations"
        """
        insert_contract_factory_fa2_operations(
            """the rows to be inserted"""
            objects: [contract_factory_fa2_operations_insert_input!]!

            """upsert condition"""
            on_conflict: contract_factory_fa2_operations_on_conflict
        ): contract_factory_fa2_operations_mutation_response

        """
        insert a single row Into the table: "contract_factory_fa2_operations"
        """
        insert_contract_factory_fa2_operations_one(
            """the row to be inserted"""
            object: contract_factory_fa2_operations_insert_input!

            """upsert condition"""
            on_conflict: contract_factory_fa2_operations_on_conflict
        ): contract_factory_fa2_operations

        """
        insert data Into the table: "contract_factory_fa2_storage"
        """
        insert_contract_factory_fa2_storage(
            """the rows to be inserted"""
            objects: [contract_factory_fa2_storage_insert_input!]!

            """upsert condition"""
            on_conflict: contract_factory_fa2_storage_on_conflict
        ): contract_factory_fa2_storage_mutation_response

        """
        insert a single row Into the table: "contract_factory_fa2_storage"
        """
        insert_contract_factory_fa2_storage_one(
            """the row to be inserted"""
            object: contract_factory_fa2_storage_insert_input!

            """upsert condition"""
            on_conflict: contract_factory_fa2_storage_on_conflict
        ): contract_factory_fa2_storage

        """
        insert data Into the table: "contract_farms_v1_operations"
        """
        insert_contract_farms_v1_operations(
            """the rows to be inserted"""
            objects: [contract_farms_v1_operations_insert_input!]!

            """upsert condition"""
            on_conflict: contract_farms_v1_operations_on_conflict
        ): contract_farms_v1_operations_mutation_response

        """
        insert a single row Into the table: "contract_farms_v1_operations"
        """
        insert_contract_farms_v1_operations_one(
            """the row to be inserted"""
            object: contract_farms_v1_operations_insert_input!

            """upsert condition"""
            on_conflict: contract_farms_v1_operations_on_conflict
        ): contract_farms_v1_operations

        """
        insert data Into the table: "contract_farms_v1_storage"
        """
        insert_contract_farms_v1_storage(
            """the rows to be inserted"""
            objects: [contract_farms_v1_storage_insert_input!]!

            """upsert condition"""
            on_conflict: contract_farms_v1_storage_on_conflict
        ): contract_farms_v1_storage_mutation_response

        """
        insert a single row Into the table: "contract_farms_v1_storage"
        """
        insert_contract_farms_v1_storage_one(
            """the row to be inserted"""
            object: contract_farms_v1_storage_insert_input!

            """upsert condition"""
            on_conflict: contract_farms_v1_storage_on_conflict
        ): contract_farms_v1_storage

        """
        insert data Into the table: "contract_farms_v2_allfarms"
        """
        insert_contract_farms_v2_allfarms(
            """the rows to be inserted"""
            objects: [contract_farms_v2_allfarms_insert_input!]!

            """upsert condition"""
            on_conflict: contract_farms_v2_allfarms_on_conflict
        ): contract_farms_v2_allfarms_mutation_response

        """
        insert a single row Into the table: "contract_farms_v2_allfarms"
        """
        insert_contract_farms_v2_allfarms_one(
            """the row to be inserted"""
            object: contract_farms_v2_allfarms_insert_input!

            """upsert condition"""
            on_conflict: contract_farms_v2_allfarms_on_conflict
        ): contract_farms_v2_allfarms

        """
        insert data Into the table: "contract_farms_v2_operations"
        """
        insert_contract_farms_v2_operations(
            """the rows to be inserted"""
            objects: [contract_farms_v2_operations_insert_input!]!

            """upsert condition"""
            on_conflict: contract_farms_v2_operations_on_conflict
        ): contract_farms_v2_operations_mutation_response

        """
        insert a single row Into the table: "contract_farms_v2_operations"
        """
        insert_contract_farms_v2_operations_one(
            """the row to be inserted"""
            object: contract_farms_v2_operations_insert_input!

            """upsert condition"""
            on_conflict: contract_farms_v2_operations_on_conflict
        ): contract_farms_v2_operations

        """
        insert data Into the table: "contract_farms_v2_storage"
        """
        insert_contract_farms_v2_storage(
            """the rows to be inserted"""
            objects: [contract_farms_v2_storage_insert_input!]!

            """upsert condition"""
            on_conflict: contract_farms_v2_storage_on_conflict
        ): contract_farms_v2_storage_mutation_response

        """
        insert a single row Into the table: "contract_farms_v2_storage"
        """
        insert_contract_farms_v2_storage_one(
            """the row to be inserted"""
            object: contract_farms_v2_storage_insert_input!

            """upsert condition"""
            on_conflict: contract_farms_v2_storage_on_conflict
        ): contract_farms_v2_storage

        """
        insert data Into the table: "contract_staking_smak_operations"
        """
        insert_contract_staking_smak_operations(
            """the rows to be inserted"""
            objects: [contract_staking_smak_operations_insert_input!]!

            """upsert condition"""
            on_conflict: contract_staking_smak_operations_on_conflict
        ): contract_staking_smak_operations_mutation_response

        """
        insert a single row Into the table: "contract_staking_smak_operations"
        """
        insert_contract_staking_smak_operations_one(
            """the row to be inserted"""
            object: contract_staking_smak_operations_insert_input!

            """upsert condition"""
            on_conflict: contract_staking_smak_operations_on_conflict
        ): contract_staking_smak_operations

        """
        insert data Into the table: "contract_staking_smak_storage"
        """
        insert_contract_staking_smak_storage(
            """the rows to be inserted"""
            objects: [contract_staking_smak_storage_insert_input!]!

            """upsert condition"""
            on_conflict: contract_staking_smak_storage_on_conflict
        ): contract_staking_smak_storage_mutation_response

        """
        insert a single row Into the table: "contract_staking_smak_storage"
        """
        insert_contract_staking_smak_storage_one(
            """the row to be inserted"""
            object: contract_staking_smak_storage_insert_input!

            """upsert condition"""
            on_conflict: contract_staking_smak_storage_on_conflict
        ): contract_staking_smak_storage

        """
        insert data Into the table: "contract_token_anti_operations"
        """
        insert_contract_token_anti_operations(
            """the rows to be inserted"""
            objects: [contract_token_anti_operations_insert_input!]!

            """upsert condition"""
            on_conflict: contract_token_anti_operations_on_conflict
        ): contract_token_anti_operations_mutation_response

        """
        insert a single row Into the table: "contract_token_anti_operations"
        """
        insert_contract_token_anti_operations_one(
            """the row to be inserted"""
            object: contract_token_anti_operations_insert_input!

            """upsert condition"""
            on_conflict: contract_token_anti_operations_on_conflict
        ): contract_token_anti_operations

        """
        insert data Into the table: "contract_token_anti_storage"
        """
        insert_contract_token_anti_storage(
            """the rows to be inserted"""
            objects: [contract_token_anti_storage_insert_input!]!

            """upsert condition"""
            on_conflict: contract_token_anti_storage_on_conflict
        ): contract_token_anti_storage_mutation_response

        """
        insert a single row Into the table: "contract_token_anti_storage"
        """
        insert_contract_token_anti_storage_one(
            """the row to be inserted"""
            object: contract_token_anti_storage_insert_input!

            """upsert condition"""
            on_conflict: contract_token_anti_storage_on_conflict
        ): contract_token_anti_storage

        """
        insert data Into the table: "contract_token_smak_operations"
        """
        insert_contract_token_smak_operations(
            """the rows to be inserted"""
            objects: [contract_token_smak_operations_insert_input!]!

            """upsert condition"""
            on_conflict: contract_token_smak_operations_on_conflict
        ): contract_token_smak_operations_mutation_response

        """
        insert a single row Into the table: "contract_token_smak_operations"
        """
        insert_contract_token_smak_operations_one(
            """the row to be inserted"""
            object: contract_token_smak_operations_insert_input!

            """upsert condition"""
            on_conflict: contract_token_smak_operations_on_conflict
        ): contract_token_smak_operations

        """
        insert data Into the table: "contract_token_smak_storage"
        """
        insert_contract_token_smak_storage(
            """the rows to be inserted"""
            objects: [contract_token_smak_storage_insert_input!]!

            """upsert condition"""
            on_conflict: contract_token_smak_storage_on_conflict
        ): contract_token_smak_storage_mutation_response

        """
        insert a single row Into the table: "contract_token_smak_storage"
        """
        insert_contract_token_smak_storage_one(
            """the row to be inserted"""
            object: contract_token_smak_storage_insert_input!

            """upsert condition"""
            on_conflict: contract_token_smak_storage_on_conflict
        ): contract_token_smak_storage

        """
        insert data Into the table: "indexer"
        """
        insert_indexer(
            """the rows to be inserted"""
            objects: [indexer_insert_input!]!

            """upsert condition"""
            on_conflict: indexer_on_conflict
        ): indexer_mutation_response

        """
        insert a single row Into the table: "indexer"
        """
        insert_indexer_one(
            """the row to be inserted"""
            object: indexer_insert_input!

            """upsert condition"""
            on_conflict: indexer_on_conflict
        ): indexer

        """
        update data of the table: "contract_dex_operations"
        """
        update_contract_dex_operations(
            """increments the numeric columns with given value of the filtered values"""
            _inc: contract_dex_operations_inc_input

            """sets the columns of the filtered rows to the given values"""
            _set: contract_dex_operations_set_input

            """filter the rows which have to be updated"""
            where: contract_dex_operations_bool_exp!
        ): contract_dex_operations_mutation_response

        """
        update single row of the table: "contract_dex_operations"
        """
        update_contract_dex_operations_by_pk(
            """increments the numeric columns with given value of the filtered values"""
            _inc: contract_dex_operations_inc_input

            """sets the columns of the filtered rows to the given values"""
            _set: contract_dex_operations_set_input
            pk_columns: contract_dex_operations_pk_columns_input!
        ): contract_dex_operations

        """
        update multiples rows of table: "contract_dex_operations"
        """
        update_contract_dex_operations_many(
            """updates to execute, in order"""
            updates: [contract_dex_operations_updates!]!
        ): [contract_dex_operations_mutation_response]

        """
        update data of the table: "contract_dex_storage"
        """
        update_contract_dex_storage(
            """increments the numeric columns with given value of the filtered values"""
            _inc: contract_dex_storage_inc_input

            """sets the columns of the filtered rows to the given values"""
            _set: contract_dex_storage_set_input

            """filter the rows which have to be updated"""
            where: contract_dex_storage_bool_exp!
        ): contract_dex_storage_mutation_response

        """
        update single row of the table: "contract_dex_storage"
        """
        update_contract_dex_storage_by_pk(
            """increments the numeric columns with given value of the filtered values"""
            _inc: contract_dex_storage_inc_input

            """sets the columns of the filtered rows to the given values"""
            _set: contract_dex_storage_set_input
            pk_columns: contract_dex_storage_pk_columns_input!
        ): contract_dex_storage

        """
        update multiples rows of table: "contract_dex_storage"
        """
        update_contract_dex_storage_many(
            """updates to execute, in order"""
            updates: [contract_dex_storage_updates!]!
        ): [contract_dex_storage_mutation_response]

        """
        update data of the table: "contract_factory_doga_operations"
        """
        update_contract_factory_doga_operations(
            """increments the numeric columns with given value of the filtered values"""
            _inc: contract_factory_doga_operations_inc_input

            """sets the columns of the filtered rows to the given values"""
            _set: contract_factory_doga_operations_set_input

            """filter the rows which have to be updated"""
            where: contract_factory_doga_operations_bool_exp!
        ): contract_factory_doga_operations_mutation_response

        """
        update single row of the table: "contract_factory_doga_operations"
        """
        update_contract_factory_doga_operations_by_pk(
            """increments the numeric columns with given value of the filtered values"""
            _inc: contract_factory_doga_operations_inc_input

            """sets the columns of the filtered rows to the given values"""
            _set: contract_factory_doga_operations_set_input
            pk_columns: contract_factory_doga_operations_pk_columns_input!
        ): contract_factory_doga_operations

        """
        update multiples rows of table: "contract_factory_doga_operations"
        """
        update_contract_factory_doga_operations_many(
            """updates to execute, in order"""
            updates: [contract_factory_doga_operations_updates!]!
        ): [contract_factory_doga_operations_mutation_response]

        """
        update data of the table: "contract_factory_doga_storage"
        """
        update_contract_factory_doga_storage(
            """increments the numeric columns with given value of the filtered values"""
            _inc: contract_factory_doga_storage_inc_input

            """sets the columns of the filtered rows to the given values"""
            _set: contract_factory_doga_storage_set_input

            """filter the rows which have to be updated"""
            where: contract_factory_doga_storage_bool_exp!
        ): contract_factory_doga_storage_mutation_response

        """
        update single row of the table: "contract_factory_doga_storage"
        """
        update_contract_factory_doga_storage_by_pk(
            """increments the numeric columns with given value of the filtered values"""
            _inc: contract_factory_doga_storage_inc_input

            """sets the columns of the filtered rows to the given values"""
            _set: contract_factory_doga_storage_set_input
            pk_columns: contract_factory_doga_storage_pk_columns_input!
        ): contract_factory_doga_storage

        """
        update multiples rows of table: "contract_factory_doga_storage"
        """
        update_contract_factory_doga_storage_many(
            """updates to execute, in order"""
            updates: [contract_factory_doga_storage_updates!]!
        ): [contract_factory_doga_storage_mutation_response]

        """
        update data of the table: "contract_factory_fa12_operations"
        """
        update_contract_factory_fa12_operations(
            """increments the numeric columns with given value of the filtered values"""
            _inc: contract_factory_fa12_operations_inc_input

            """sets the columns of the filtered rows to the given values"""
            _set: contract_factory_fa12_operations_set_input

            """filter the rows which have to be updated"""
            where: contract_factory_fa12_operations_bool_exp!
        ): contract_factory_fa12_operations_mutation_response

        """
        update single row of the table: "contract_factory_fa12_operations"
        """
        update_contract_factory_fa12_operations_by_pk(
            """increments the numeric columns with given value of the filtered values"""
            _inc: contract_factory_fa12_operations_inc_input

            """sets the columns of the filtered rows to the given values"""
            _set: contract_factory_fa12_operations_set_input
            pk_columns: contract_factory_fa12_operations_pk_columns_input!
        ): contract_factory_fa12_operations

        """
        update multiples rows of table: "contract_factory_fa12_operations"
        """
        update_contract_factory_fa12_operations_many(
            """updates to execute, in order"""
            updates: [contract_factory_fa12_operations_updates!]!
        ): [contract_factory_fa12_operations_mutation_response]

        """
        update data of the table: "contract_factory_fa12_storage"
        """
        update_contract_factory_fa12_storage(
            """increments the numeric columns with given value of the filtered values"""
            _inc: contract_factory_fa12_storage_inc_input

            """sets the columns of the filtered rows to the given values"""
            _set: contract_factory_fa12_storage_set_input

            """filter the rows which have to be updated"""
            where: contract_factory_fa12_storage_bool_exp!
        ): contract_factory_fa12_storage_mutation_response

        """
        update single row of the table: "contract_factory_fa12_storage"
        """
        update_contract_factory_fa12_storage_by_pk(
            """increments the numeric columns with given value of the filtered values"""
            _inc: contract_factory_fa12_storage_inc_input

            """sets the columns of the filtered rows to the given values"""
            _set: contract_factory_fa12_storage_set_input
            pk_columns: contract_factory_fa12_storage_pk_columns_input!
        ): contract_factory_fa12_storage

        """
        update multiples rows of table: "contract_factory_fa12_storage"
        """
        update_contract_factory_fa12_storage_many(
            """updates to execute, in order"""
            updates: [contract_factory_fa12_storage_updates!]!
        ): [contract_factory_fa12_storage_mutation_response]

        """
        update data of the table: "contract_factory_fa2_operations"
        """
        update_contract_factory_fa2_operations(
            """increments the numeric columns with given value of the filtered values"""
            _inc: contract_factory_fa2_operations_inc_input

            """sets the columns of the filtered rows to the given values"""
            _set: contract_factory_fa2_operations_set_input

            """filter the rows which have to be updated"""
            where: contract_factory_fa2_operations_bool_exp!
        ): contract_factory_fa2_operations_mutation_response

        """
        update single row of the table: "contract_factory_fa2_operations"
        """
        update_contract_factory_fa2_operations_by_pk(
            """increments the numeric columns with given value of the filtered values"""
            _inc: contract_factory_fa2_operations_inc_input

            """sets the columns of the filtered rows to the given values"""
            _set: contract_factory_fa2_operations_set_input
            pk_columns: contract_factory_fa2_operations_pk_columns_input!
        ): contract_factory_fa2_operations

        """
        update multiples rows of table: "contract_factory_fa2_operations"
        """
        update_contract_factory_fa2_operations_many(
            """updates to execute, in order"""
            updates: [contract_factory_fa2_operations_updates!]!
        ): [contract_factory_fa2_operations_mutation_response]

        """
        update data of the table: "contract_factory_fa2_storage"
        """
        update_contract_factory_fa2_storage(
            """increments the numeric columns with given value of the filtered values"""
            _inc: contract_factory_fa2_storage_inc_input

            """sets the columns of the filtered rows to the given values"""
            _set: contract_factory_fa2_storage_set_input

            """filter the rows which have to be updated"""
            where: contract_factory_fa2_storage_bool_exp!
        ): contract_factory_fa2_storage_mutation_response

        """
        update single row of the table: "contract_factory_fa2_storage"
        """
        update_contract_factory_fa2_storage_by_pk(
            """increments the numeric columns with given value of the filtered values"""
            _inc: contract_factory_fa2_storage_inc_input

            """sets the columns of the filtered rows to the given values"""
            _set: contract_factory_fa2_storage_set_input
            pk_columns: contract_factory_fa2_storage_pk_columns_input!
        ): contract_factory_fa2_storage

        """
        update multiples rows of table: "contract_factory_fa2_storage"
        """
        update_contract_factory_fa2_storage_many(
            """updates to execute, in order"""
            updates: [contract_factory_fa2_storage_updates!]!
        ): [contract_factory_fa2_storage_mutation_response]

        """
        update data of the table: "contract_farms_v1_operations"
        """
        update_contract_farms_v1_operations(
            """increments the numeric columns with given value of the filtered values"""
            _inc: contract_farms_v1_operations_inc_input

            """sets the columns of the filtered rows to the given values"""
            _set: contract_farms_v1_operations_set_input

            """filter the rows which have to be updated"""
            where: contract_farms_v1_operations_bool_exp!
        ): contract_farms_v1_operations_mutation_response

        """
        update single row of the table: "contract_farms_v1_operations"
        """
        update_contract_farms_v1_operations_by_pk(
            """increments the numeric columns with given value of the filtered values"""
            _inc: contract_farms_v1_operations_inc_input

            """sets the columns of the filtered rows to the given values"""
            _set: contract_farms_v1_operations_set_input
            pk_columns: contract_farms_v1_operations_pk_columns_input!
        ): contract_farms_v1_operations

        """
        update multiples rows of table: "contract_farms_v1_operations"
        """
        update_contract_farms_v1_operations_many(
            """updates to execute, in order"""
            updates: [contract_farms_v1_operations_updates!]!
        ): [contract_farms_v1_operations_mutation_response]

        """
        update data of the table: "contract_farms_v1_storage"
        """
        update_contract_farms_v1_storage(
            """increments the numeric columns with given value of the filtered values"""
            _inc: contract_farms_v1_storage_inc_input

            """sets the columns of the filtered rows to the given values"""
            _set: contract_farms_v1_storage_set_input

            """filter the rows which have to be updated"""
            where: contract_farms_v1_storage_bool_exp!
        ): contract_farms_v1_storage_mutation_response

        """
        update single row of the table: "contract_farms_v1_storage"
        """
        update_contract_farms_v1_storage_by_pk(
            """increments the numeric columns with given value of the filtered values"""
            _inc: contract_farms_v1_storage_inc_input

            """sets the columns of the filtered rows to the given values"""
            _set: contract_farms_v1_storage_set_input
            pk_columns: contract_farms_v1_storage_pk_columns_input!
        ): contract_farms_v1_storage

        """
        update multiples rows of table: "contract_farms_v1_storage"
        """
        update_contract_farms_v1_storage_many(
            """updates to execute, in order"""
            updates: [contract_farms_v1_storage_updates!]!
        ): [contract_farms_v1_storage_mutation_response]

        """
        update data of the table: "contract_farms_v2_allfarms"
        """
        update_contract_farms_v2_allfarms(
            """increments the numeric columns with given value of the filtered values"""
            _inc: contract_farms_v2_allfarms_inc_input

            """sets the columns of the filtered rows to the given values"""
            _set: contract_farms_v2_allfarms_set_input

            """filter the rows which have to be updated"""
            where: contract_farms_v2_allfarms_bool_exp!
        ): contract_farms_v2_allfarms_mutation_response

        """
        update single row of the table: "contract_farms_v2_allfarms"
        """
        update_contract_farms_v2_allfarms_by_pk(
            """increments the numeric columns with given value of the filtered values"""
            _inc: contract_farms_v2_allfarms_inc_input

            """sets the columns of the filtered rows to the given values"""
            _set: contract_farms_v2_allfarms_set_input
            pk_columns: contract_farms_v2_allfarms_pk_columns_input!
        ): contract_farms_v2_allfarms

        """
        update multiples rows of table: "contract_farms_v2_allfarms"
        """
        update_contract_farms_v2_allfarms_many(
            """updates to execute, in order"""
            updates: [contract_farms_v2_allfarms_updates!]!
        ): [contract_farms_v2_allfarms_mutation_response]

        """
        update data of the table: "contract_farms_v2_operations"
        """
        update_contract_farms_v2_operations(
            """increments the numeric columns with given value of the filtered values"""
            _inc: contract_farms_v2_operations_inc_input

            """sets the columns of the filtered rows to the given values"""
            _set: contract_farms_v2_operations_set_input

            """filter the rows which have to be updated"""
            where: contract_farms_v2_operations_bool_exp!
        ): contract_farms_v2_operations_mutation_response

        """
        update single row of the table: "contract_farms_v2_operations"
        """
        update_contract_farms_v2_operations_by_pk(
            """increments the numeric columns with given value of the filtered values"""
            _inc: contract_farms_v2_operations_inc_input

            """sets the columns of the filtered rows to the given values"""
            _set: contract_farms_v2_operations_set_input
            pk_columns: contract_farms_v2_operations_pk_columns_input!
        ): contract_farms_v2_operations

        """
        update multiples rows of table: "contract_farms_v2_operations"
        """
        update_contract_farms_v2_operations_many(
            """updates to execute, in order"""
            updates: [contract_farms_v2_operations_updates!]!
        ): [contract_farms_v2_operations_mutation_response]

        """
        update data of the table: "contract_farms_v2_storage"
        """
        update_contract_farms_v2_storage(
            """increments the numeric columns with given value of the filtered values"""
            _inc: contract_farms_v2_storage_inc_input

            """sets the columns of the filtered rows to the given values"""
            _set: contract_farms_v2_storage_set_input

            """filter the rows which have to be updated"""
            where: contract_farms_v2_storage_bool_exp!
        ): contract_farms_v2_storage_mutation_response

        """
        update single row of the table: "contract_farms_v2_storage"
        """
        update_contract_farms_v2_storage_by_pk(
            """increments the numeric columns with given value of the filtered values"""
            _inc: contract_farms_v2_storage_inc_input

            """sets the columns of the filtered rows to the given values"""
            _set: contract_farms_v2_storage_set_input
            pk_columns: contract_farms_v2_storage_pk_columns_input!
        ): contract_farms_v2_storage

        """
        update multiples rows of table: "contract_farms_v2_storage"
        """
        update_contract_farms_v2_storage_many(
            """updates to execute, in order"""
            updates: [contract_farms_v2_storage_updates!]!
        ): [contract_farms_v2_storage_mutation_response]

        """
        update data of the table: "contract_staking_smak_operations"
        """
        update_contract_staking_smak_operations(
            """increments the numeric columns with given value of the filtered values"""
            _inc: contract_staking_smak_operations_inc_input

            """sets the columns of the filtered rows to the given values"""
            _set: contract_staking_smak_operations_set_input

            """filter the rows which have to be updated"""
            where: contract_staking_smak_operations_bool_exp!
        ): contract_staking_smak_operations_mutation_response

        """
        update single row of the table: "contract_staking_smak_operations"
        """
        update_contract_staking_smak_operations_by_pk(
            """increments the numeric columns with given value of the filtered values"""
            _inc: contract_staking_smak_operations_inc_input

            """sets the columns of the filtered rows to the given values"""
            _set: contract_staking_smak_operations_set_input
            pk_columns: contract_staking_smak_operations_pk_columns_input!
        ): contract_staking_smak_operations

        """
        update multiples rows of table: "contract_staking_smak_operations"
        """
        update_contract_staking_smak_operations_many(
            """updates to execute, in order"""
            updates: [contract_staking_smak_operations_updates!]!
        ): [contract_staking_smak_operations_mutation_response]

        """
        update data of the table: "contract_staking_smak_storage"
        """
        update_contract_staking_smak_storage(
            """increments the numeric columns with given value of the filtered values"""
            _inc: contract_staking_smak_storage_inc_input

            """sets the columns of the filtered rows to the given values"""
            _set: contract_staking_smak_storage_set_input

            """filter the rows which have to be updated"""
            where: contract_staking_smak_storage_bool_exp!
        ): contract_staking_smak_storage_mutation_response

        """
        update single row of the table: "contract_staking_smak_storage"
        """
        update_contract_staking_smak_storage_by_pk(
            """increments the numeric columns with given value of the filtered values"""
            _inc: contract_staking_smak_storage_inc_input

            """sets the columns of the filtered rows to the given values"""
            _set: contract_staking_smak_storage_set_input
            pk_columns: contract_staking_smak_storage_pk_columns_input!
        ): contract_staking_smak_storage

        """
        update multiples rows of table: "contract_staking_smak_storage"
        """
        update_contract_staking_smak_storage_many(
            """updates to execute, in order"""
            updates: [contract_staking_smak_storage_updates!]!
        ): [contract_staking_smak_storage_mutation_response]

        """
        update data of the table: "contract_token_anti_operations"
        """
        update_contract_token_anti_operations(
            """increments the numeric columns with given value of the filtered values"""
            _inc: contract_token_anti_operations_inc_input

            """sets the columns of the filtered rows to the given values"""
            _set: contract_token_anti_operations_set_input

            """filter the rows which have to be updated"""
            where: contract_token_anti_operations_bool_exp!
        ): contract_token_anti_operations_mutation_response

        """
        update single row of the table: "contract_token_anti_operations"
        """
        update_contract_token_anti_operations_by_pk(
            """increments the numeric columns with given value of the filtered values"""
            _inc: contract_token_anti_operations_inc_input

            """sets the columns of the filtered rows to the given values"""
            _set: contract_token_anti_operations_set_input
            pk_columns: contract_token_anti_operations_pk_columns_input!
        ): contract_token_anti_operations

        """
        update multiples rows of table: "contract_token_anti_operations"
        """
        update_contract_token_anti_operations_many(
            """updates to execute, in order"""
            updates: [contract_token_anti_operations_updates!]!
        ): [contract_token_anti_operations_mutation_response]

        """
        update data of the table: "contract_token_anti_storage"
        """
        update_contract_token_anti_storage(
            """increments the numeric columns with given value of the filtered values"""
            _inc: contract_token_anti_storage_inc_input

            """sets the columns of the filtered rows to the given values"""
            _set: contract_token_anti_storage_set_input

            """filter the rows which have to be updated"""
            where: contract_token_anti_storage_bool_exp!
        ): contract_token_anti_storage_mutation_response

        """
        update single row of the table: "contract_token_anti_storage"
        """
        update_contract_token_anti_storage_by_pk(
            """increments the numeric columns with given value of the filtered values"""
            _inc: contract_token_anti_storage_inc_input

            """sets the columns of the filtered rows to the given values"""
            _set: contract_token_anti_storage_set_input
            pk_columns: contract_token_anti_storage_pk_columns_input!
        ): contract_token_anti_storage

        """
        update multiples rows of table: "contract_token_anti_storage"
        """
        update_contract_token_anti_storage_many(
            """updates to execute, in order"""
            updates: [contract_token_anti_storage_updates!]!
        ): [contract_token_anti_storage_mutation_response]

        """
        update data of the table: "contract_token_smak_operations"
        """
        update_contract_token_smak_operations(
            """increments the numeric columns with given value of the filtered values"""
            _inc: contract_token_smak_operations_inc_input

            """sets the columns of the filtered rows to the given values"""
            _set: contract_token_smak_operations_set_input

            """filter the rows which have to be updated"""
            where: contract_token_smak_operations_bool_exp!
        ): contract_token_smak_operations_mutation_response

        """
        update single row of the table: "contract_token_smak_operations"
        """
        update_contract_token_smak_operations_by_pk(
            """increments the numeric columns with given value of the filtered values"""
            _inc: contract_token_smak_operations_inc_input

            """sets the columns of the filtered rows to the given values"""
            _set: contract_token_smak_operations_set_input
            pk_columns: contract_token_smak_operations_pk_columns_input!
        ): contract_token_smak_operations

        """
        update multiples rows of table: "contract_token_smak_operations"
        """
        update_contract_token_smak_operations_many(
            """updates to execute, in order"""
            updates: [contract_token_smak_operations_updates!]!
        ): [contract_token_smak_operations_mutation_response]

        """
        update data of the table: "contract_token_smak_storage"
        """
        update_contract_token_smak_storage(
            """increments the numeric columns with given value of the filtered values"""
            _inc: contract_token_smak_storage_inc_input

            """sets the columns of the filtered rows to the given values"""
            _set: contract_token_smak_storage_set_input

            """filter the rows which have to be updated"""
            where: contract_token_smak_storage_bool_exp!
        ): contract_token_smak_storage_mutation_response

        """
        update single row of the table: "contract_token_smak_storage"
        """
        update_contract_token_smak_storage_by_pk(
            """increments the numeric columns with given value of the filtered values"""
            _inc: contract_token_smak_storage_inc_input

            """sets the columns of the filtered rows to the given values"""
            _set: contract_token_smak_storage_set_input
            pk_columns: contract_token_smak_storage_pk_columns_input!
        ): contract_token_smak_storage

        """
        update multiples rows of table: "contract_token_smak_storage"
        """
        update_contract_token_smak_storage_many(
            """updates to execute, in order"""
            updates: [contract_token_smak_storage_updates!]!
        ): [contract_token_smak_storage_mutation_response]

        """
        update data of the table: "indexer"
        """
        update_indexer(
            """increments the numeric columns with given value of the filtered values"""
            _inc: indexer_inc_input

            """sets the columns of the filtered rows to the given values"""
            _set: indexer_set_input

            """filter the rows which have to be updated"""
            where: indexer_bool_exp!
        ): indexer_mutation_response

        """
        update single row of the table: "indexer"
        """
        update_indexer_by_pk(
            """increments the numeric columns with given value of the filtered values"""
            _inc: indexer_inc_input

            """sets the columns of the filtered rows to the given values"""
            _set: indexer_set_input
            pk_columns: indexer_pk_columns_input!
        ): indexer

        """
        update multiples rows of table: "indexer"
        """
        update_indexer_many(
            """updates to execute, in order"""
            updates: [indexer_updates!]!
        ): [indexer_mutation_response]
        }

        """column ordering options"""
        enum order_by {
        """in ascending order, nulls last"""
        asc

        """in ascending order, nulls first"""
        asc_nulls_first

        """in ascending order, nulls last"""
        asc_nulls_last

        """in descending order, nulls first"""
        desc

        """in descending order, nulls first"""
        desc_nulls_first

        """in descending order, nulls last"""
        desc_nulls_last
        }

        type query_root {
        """
        fetch data from the table: "contract_dex_operations"
        """
        contract_dex_operations(
            """distinct select on columns"""
            distinct_on: [contract_dex_operations_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_dex_operations_order_by!]

            """filter the rows returned"""
            where: contract_dex_operations_bool_exp
        ): [contract_dex_operations!]!

        """
        fetch aggregated fields from the table: "contract_dex_operations"
        """
        contract_dex_operations_aggregate(
            """distinct select on columns"""
            distinct_on: [contract_dex_operations_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_dex_operations_order_by!]

            """filter the rows returned"""
            where: contract_dex_operations_bool_exp
        ): contract_dex_operations_aggregate!

        """
        fetch data from the table: "contract_dex_operations" using primary key columns
        """
        contract_dex_operations_by_pk(id: Int!): contract_dex_operations

        """
        fetch data from the table: "contract_dex_storage"
        """
        contract_dex_storage(
            """distinct select on columns"""
            distinct_on: [contract_dex_storage_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_dex_storage_order_by!]

            """filter the rows returned"""
            where: contract_dex_storage_bool_exp
        ): [contract_dex_storage!]!

        """
        fetch aggregated fields from the table: "contract_dex_storage"
        """
        contract_dex_storage_aggregate(
            """distinct select on columns"""
            distinct_on: [contract_dex_storage_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_dex_storage_order_by!]

            """filter the rows returned"""
            where: contract_dex_storage_bool_exp
        ): contract_dex_storage_aggregate!

        """
        fetch data from the table: "contract_dex_storage" using primary key columns
        """
        contract_dex_storage_by_pk(id: Int!): contract_dex_storage

        """
        fetch data from the table: "contract_factory_doga_operations"
        """
        contract_factory_doga_operations(
            """distinct select on columns"""
            distinct_on: [contract_factory_doga_operations_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_factory_doga_operations_order_by!]

            """filter the rows returned"""
            where: contract_factory_doga_operations_bool_exp
        ): [contract_factory_doga_operations!]!

        """
        fetch aggregated fields from the table: "contract_factory_doga_operations"
        """
        contract_factory_doga_operations_aggregate(
            """distinct select on columns"""
            distinct_on: [contract_factory_doga_operations_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_factory_doga_operations_order_by!]

            """filter the rows returned"""
            where: contract_factory_doga_operations_bool_exp
        ): contract_factory_doga_operations_aggregate!

        """
        fetch data from the table: "contract_factory_doga_operations" using primary key columns
        """
        contract_factory_doga_operations_by_pk(id: Int!): contract_factory_doga_operations

        """
        fetch data from the table: "contract_factory_doga_storage"
        """
        contract_factory_doga_storage(
            """distinct select on columns"""
            distinct_on: [contract_factory_doga_storage_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_factory_doga_storage_order_by!]

            """filter the rows returned"""
            where: contract_factory_doga_storage_bool_exp
        ): [contract_factory_doga_storage!]!

        """
        fetch aggregated fields from the table: "contract_factory_doga_storage"
        """
        contract_factory_doga_storage_aggregate(
            """distinct select on columns"""
            distinct_on: [contract_factory_doga_storage_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_factory_doga_storage_order_by!]

            """filter the rows returned"""
            where: contract_factory_doga_storage_bool_exp
        ): contract_factory_doga_storage_aggregate!

        """
        fetch data from the table: "contract_factory_doga_storage" using primary key columns
        """
        contract_factory_doga_storage_by_pk(id: Int!): contract_factory_doga_storage

        """
        fetch data from the table: "contract_factory_fa12_operations"
        """
        contract_factory_fa12_operations(
            """distinct select on columns"""
            distinct_on: [contract_factory_fa12_operations_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_factory_fa12_operations_order_by!]

            """filter the rows returned"""
            where: contract_factory_fa12_operations_bool_exp
        ): [contract_factory_fa12_operations!]!

        """
        fetch aggregated fields from the table: "contract_factory_fa12_operations"
        """
        contract_factory_fa12_operations_aggregate(
            """distinct select on columns"""
            distinct_on: [contract_factory_fa12_operations_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_factory_fa12_operations_order_by!]

            """filter the rows returned"""
            where: contract_factory_fa12_operations_bool_exp
        ): contract_factory_fa12_operations_aggregate!

        """
        fetch data from the table: "contract_factory_fa12_operations" using primary key columns
        """
        contract_factory_fa12_operations_by_pk(id: Int!): contract_factory_fa12_operations

        """
        fetch data from the table: "contract_factory_fa12_storage"
        """
        contract_factory_fa12_storage(
            """distinct select on columns"""
            distinct_on: [contract_factory_fa12_storage_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_factory_fa12_storage_order_by!]

            """filter the rows returned"""
            where: contract_factory_fa12_storage_bool_exp
        ): [contract_factory_fa12_storage!]!

        """
        fetch aggregated fields from the table: "contract_factory_fa12_storage"
        """
        contract_factory_fa12_storage_aggregate(
            """distinct select on columns"""
            distinct_on: [contract_factory_fa12_storage_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_factory_fa12_storage_order_by!]

            """filter the rows returned"""
            where: contract_factory_fa12_storage_bool_exp
        ): contract_factory_fa12_storage_aggregate!

        """
        fetch data from the table: "contract_factory_fa12_storage" using primary key columns
        """
        contract_factory_fa12_storage_by_pk(id: Int!): contract_factory_fa12_storage

        """
        fetch data from the table: "contract_factory_fa2_operations"
        """
        contract_factory_fa2_operations(
            """distinct select on columns"""
            distinct_on: [contract_factory_fa2_operations_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_factory_fa2_operations_order_by!]

            """filter the rows returned"""
            where: contract_factory_fa2_operations_bool_exp
        ): [contract_factory_fa2_operations!]!

        """
        fetch aggregated fields from the table: "contract_factory_fa2_operations"
        """
        contract_factory_fa2_operations_aggregate(
            """distinct select on columns"""
            distinct_on: [contract_factory_fa2_operations_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_factory_fa2_operations_order_by!]

            """filter the rows returned"""
            where: contract_factory_fa2_operations_bool_exp
        ): contract_factory_fa2_operations_aggregate!

        """
        fetch data from the table: "contract_factory_fa2_operations" using primary key columns
        """
        contract_factory_fa2_operations_by_pk(id: Int!): contract_factory_fa2_operations

        """
        fetch data from the table: "contract_factory_fa2_storage"
        """
        contract_factory_fa2_storage(
            """distinct select on columns"""
            distinct_on: [contract_factory_fa2_storage_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_factory_fa2_storage_order_by!]

            """filter the rows returned"""
            where: contract_factory_fa2_storage_bool_exp
        ): [contract_factory_fa2_storage!]!

        """
        fetch aggregated fields from the table: "contract_factory_fa2_storage"
        """
        contract_factory_fa2_storage_aggregate(
            """distinct select on columns"""
            distinct_on: [contract_factory_fa2_storage_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_factory_fa2_storage_order_by!]

            """filter the rows returned"""
            where: contract_factory_fa2_storage_bool_exp
        ): contract_factory_fa2_storage_aggregate!

        """
        fetch data from the table: "contract_factory_fa2_storage" using primary key columns
        """
        contract_factory_fa2_storage_by_pk(id: Int!): contract_factory_fa2_storage

        """
        fetch data from the table: "contract_farms_v1_operations"
        """
        contract_farms_v1_operations(
            """distinct select on columns"""
            distinct_on: [contract_farms_v1_operations_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_farms_v1_operations_order_by!]

            """filter the rows returned"""
            where: contract_farms_v1_operations_bool_exp
        ): [contract_farms_v1_operations!]!

        """
        fetch aggregated fields from the table: "contract_farms_v1_operations"
        """
        contract_farms_v1_operations_aggregate(
            """distinct select on columns"""
            distinct_on: [contract_farms_v1_operations_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_farms_v1_operations_order_by!]

            """filter the rows returned"""
            where: contract_farms_v1_operations_bool_exp
        ): contract_farms_v1_operations_aggregate!

        """
        fetch data from the table: "contract_farms_v1_operations" using primary key columns
        """
        contract_farms_v1_operations_by_pk(id: Int!): contract_farms_v1_operations

        """
        fetch data from the table: "contract_farms_v1_storage"
        """
        contract_farms_v1_storage(
            """distinct select on columns"""
            distinct_on: [contract_farms_v1_storage_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_farms_v1_storage_order_by!]

            """filter the rows returned"""
            where: contract_farms_v1_storage_bool_exp
        ): [contract_farms_v1_storage!]!

        """
        fetch aggregated fields from the table: "contract_farms_v1_storage"
        """
        contract_farms_v1_storage_aggregate(
            """distinct select on columns"""
            distinct_on: [contract_farms_v1_storage_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_farms_v1_storage_order_by!]

            """filter the rows returned"""
            where: contract_farms_v1_storage_bool_exp
        ): contract_farms_v1_storage_aggregate!

        """
        fetch data from the table: "contract_farms_v1_storage" using primary key columns
        """
        contract_farms_v1_storage_by_pk(id: Int!): contract_farms_v1_storage

        """
        fetch data from the table: "contract_farms_v2_allfarms"
        """
        contract_farms_v2_allfarms(
            """distinct select on columns"""
            distinct_on: [contract_farms_v2_allfarms_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_farms_v2_allfarms_order_by!]

            """filter the rows returned"""
            where: contract_farms_v2_allfarms_bool_exp
        ): [contract_farms_v2_allfarms!]!

        """
        fetch aggregated fields from the table: "contract_farms_v2_allfarms"
        """
        contract_farms_v2_allfarms_aggregate(
            """distinct select on columns"""
            distinct_on: [contract_farms_v2_allfarms_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_farms_v2_allfarms_order_by!]

            """filter the rows returned"""
            where: contract_farms_v2_allfarms_bool_exp
        ): contract_farms_v2_allfarms_aggregate!

        """
        fetch data from the table: "contract_farms_v2_allfarms" using primary key columns
        """
        contract_farms_v2_allfarms_by_pk(id: Int!): contract_farms_v2_allfarms

        """
        fetch data from the table: "contract_farms_v2_operations"
        """
        contract_farms_v2_operations(
            """distinct select on columns"""
            distinct_on: [contract_farms_v2_operations_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_farms_v2_operations_order_by!]

            """filter the rows returned"""
            where: contract_farms_v2_operations_bool_exp
        ): [contract_farms_v2_operations!]!

        """
        fetch aggregated fields from the table: "contract_farms_v2_operations"
        """
        contract_farms_v2_operations_aggregate(
            """distinct select on columns"""
            distinct_on: [contract_farms_v2_operations_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_farms_v2_operations_order_by!]

            """filter the rows returned"""
            where: contract_farms_v2_operations_bool_exp
        ): contract_farms_v2_operations_aggregate!

        """
        fetch data from the table: "contract_farms_v2_operations" using primary key columns
        """
        contract_farms_v2_operations_by_pk(id: Int!): contract_farms_v2_operations

        """
        fetch data from the table: "contract_farms_v2_storage"
        """
        contract_farms_v2_storage(
            """distinct select on columns"""
            distinct_on: [contract_farms_v2_storage_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_farms_v2_storage_order_by!]

            """filter the rows returned"""
            where: contract_farms_v2_storage_bool_exp
        ): [contract_farms_v2_storage!]!

        """
        fetch aggregated fields from the table: "contract_farms_v2_storage"
        """
        contract_farms_v2_storage_aggregate(
            """distinct select on columns"""
            distinct_on: [contract_farms_v2_storage_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_farms_v2_storage_order_by!]

            """filter the rows returned"""
            where: contract_farms_v2_storage_bool_exp
        ): contract_farms_v2_storage_aggregate!

        """
        fetch data from the table: "contract_farms_v2_storage" using primary key columns
        """
        contract_farms_v2_storage_by_pk(id: Int!): contract_farms_v2_storage

        """
        fetch data from the table: "contract_staking_smak_operations"
        """
        contract_staking_smak_operations(
            """distinct select on columns"""
            distinct_on: [contract_staking_smak_operations_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_staking_smak_operations_order_by!]

            """filter the rows returned"""
            where: contract_staking_smak_operations_bool_exp
        ): [contract_staking_smak_operations!]!

        """
        fetch aggregated fields from the table: "contract_staking_smak_operations"
        """
        contract_staking_smak_operations_aggregate(
            """distinct select on columns"""
            distinct_on: [contract_staking_smak_operations_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_staking_smak_operations_order_by!]

            """filter the rows returned"""
            where: contract_staking_smak_operations_bool_exp
        ): contract_staking_smak_operations_aggregate!

        """
        fetch data from the table: "contract_staking_smak_operations" using primary key columns
        """
        contract_staking_smak_operations_by_pk(id: Int!): contract_staking_smak_operations

        """
        fetch data from the table: "contract_staking_smak_storage"
        """
        contract_staking_smak_storage(
            """distinct select on columns"""
            distinct_on: [contract_staking_smak_storage_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_staking_smak_storage_order_by!]

            """filter the rows returned"""
            where: contract_staking_smak_storage_bool_exp
        ): [contract_staking_smak_storage!]!

        """
        fetch aggregated fields from the table: "contract_staking_smak_storage"
        """
        contract_staking_smak_storage_aggregate(
            """distinct select on columns"""
            distinct_on: [contract_staking_smak_storage_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_staking_smak_storage_order_by!]

            """filter the rows returned"""
            where: contract_staking_smak_storage_bool_exp
        ): contract_staking_smak_storage_aggregate!

        """
        fetch data from the table: "contract_staking_smak_storage" using primary key columns
        """
        contract_staking_smak_storage_by_pk(id: Int!): contract_staking_smak_storage

        """
        fetch data from the table: "contract_token_anti_operations"
        """
        contract_token_anti_operations(
            """distinct select on columns"""
            distinct_on: [contract_token_anti_operations_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_token_anti_operations_order_by!]

            """filter the rows returned"""
            where: contract_token_anti_operations_bool_exp
        ): [contract_token_anti_operations!]!

        """
        fetch aggregated fields from the table: "contract_token_anti_operations"
        """
        contract_token_anti_operations_aggregate(
            """distinct select on columns"""
            distinct_on: [contract_token_anti_operations_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_token_anti_operations_order_by!]

            """filter the rows returned"""
            where: contract_token_anti_operations_bool_exp
        ): contract_token_anti_operations_aggregate!

        """
        fetch data from the table: "contract_token_anti_operations" using primary key columns
        """
        contract_token_anti_operations_by_pk(id: Int!): contract_token_anti_operations

        """
        fetch data from the table: "contract_token_anti_storage"
        """
        contract_token_anti_storage(
            """distinct select on columns"""
            distinct_on: [contract_token_anti_storage_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_token_anti_storage_order_by!]

            """filter the rows returned"""
            where: contract_token_anti_storage_bool_exp
        ): [contract_token_anti_storage!]!

        """
        fetch aggregated fields from the table: "contract_token_anti_storage"
        """
        contract_token_anti_storage_aggregate(
            """distinct select on columns"""
            distinct_on: [contract_token_anti_storage_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_token_anti_storage_order_by!]

            """filter the rows returned"""
            where: contract_token_anti_storage_bool_exp
        ): contract_token_anti_storage_aggregate!

        """
        fetch data from the table: "contract_token_anti_storage" using primary key columns
        """
        contract_token_anti_storage_by_pk(id: Int!): contract_token_anti_storage

        """
        fetch data from the table: "contract_token_smak_operations"
        """
        contract_token_smak_operations(
            """distinct select on columns"""
            distinct_on: [contract_token_smak_operations_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_token_smak_operations_order_by!]

            """filter the rows returned"""
            where: contract_token_smak_operations_bool_exp
        ): [contract_token_smak_operations!]!

        """
        fetch aggregated fields from the table: "contract_token_smak_operations"
        """
        contract_token_smak_operations_aggregate(
            """distinct select on columns"""
            distinct_on: [contract_token_smak_operations_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_token_smak_operations_order_by!]

            """filter the rows returned"""
            where: contract_token_smak_operations_bool_exp
        ): contract_token_smak_operations_aggregate!

        """
        fetch data from the table: "contract_token_smak_operations" using primary key columns
        """
        contract_token_smak_operations_by_pk(id: Int!): contract_token_smak_operations

        """
        fetch data from the table: "contract_token_smak_storage"
        """
        contract_token_smak_storage(
            """distinct select on columns"""
            distinct_on: [contract_token_smak_storage_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_token_smak_storage_order_by!]

            """filter the rows returned"""
            where: contract_token_smak_storage_bool_exp
        ): [contract_token_smak_storage!]!

        """
        fetch aggregated fields from the table: "contract_token_smak_storage"
        """
        contract_token_smak_storage_aggregate(
            """distinct select on columns"""
            distinct_on: [contract_token_smak_storage_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_token_smak_storage_order_by!]

            """filter the rows returned"""
            where: contract_token_smak_storage_bool_exp
        ): contract_token_smak_storage_aggregate!

        """
        fetch data from the table: "contract_token_smak_storage" using primary key columns
        """
        contract_token_smak_storage_by_pk(id: Int!): contract_token_smak_storage

        """
        fetch data from the table: "indexer"
        """
        indexer(
            """distinct select on columns"""
            distinct_on: [indexer_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [indexer_order_by!]

            """filter the rows returned"""
            where: indexer_bool_exp
        ): [indexer!]!

        """
        fetch aggregated fields from the table: "indexer"
        """
        indexer_aggregate(
            """distinct select on columns"""
            distinct_on: [indexer_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [indexer_order_by!]

            """filter the rows returned"""
            where: indexer_bool_exp
        ): indexer_aggregate!

        """fetch data from the table: "indexer" using primary key columns"""
        indexer_by_pk(id: Int!): indexer
        }

        type subscription_root {
        """
        fetch data from the table: "contract_dex_operations"
        """
        contract_dex_operations(
            """distinct select on columns"""
            distinct_on: [contract_dex_operations_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_dex_operations_order_by!]

            """filter the rows returned"""
            where: contract_dex_operations_bool_exp
        ): [contract_dex_operations!]!

        """
        fetch aggregated fields from the table: "contract_dex_operations"
        """
        contract_dex_operations_aggregate(
            """distinct select on columns"""
            distinct_on: [contract_dex_operations_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_dex_operations_order_by!]

            """filter the rows returned"""
            where: contract_dex_operations_bool_exp
        ): contract_dex_operations_aggregate!

        """
        fetch data from the table: "contract_dex_operations" using primary key columns
        """
        contract_dex_operations_by_pk(id: Int!): contract_dex_operations

        """
        fetch data from the table in a streaming manner: "contract_dex_operations"
        """
        contract_dex_operations_stream(
            """maximum number of rows returned in a single batch"""
            batch_size: Int!

            """cursor to stream the results returned by the query"""
            cursor: [contract_dex_operations_stream_cursor_input]!

            """filter the rows returned"""
            where: contract_dex_operations_bool_exp
        ): [contract_dex_operations!]!

        """
        fetch data from the table: "contract_dex_storage"
        """
        contract_dex_storage(
            """distinct select on columns"""
            distinct_on: [contract_dex_storage_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_dex_storage_order_by!]

            """filter the rows returned"""
            where: contract_dex_storage_bool_exp
        ): [contract_dex_storage!]!

        """
        fetch aggregated fields from the table: "contract_dex_storage"
        """
        contract_dex_storage_aggregate(
            """distinct select on columns"""
            distinct_on: [contract_dex_storage_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_dex_storage_order_by!]

            """filter the rows returned"""
            where: contract_dex_storage_bool_exp
        ): contract_dex_storage_aggregate!

        """
        fetch data from the table: "contract_dex_storage" using primary key columns
        """
        contract_dex_storage_by_pk(id: Int!): contract_dex_storage

        """
        fetch data from the table in a streaming manner: "contract_dex_storage"
        """
        contract_dex_storage_stream(
            """maximum number of rows returned in a single batch"""
            batch_size: Int!

            """cursor to stream the results returned by the query"""
            cursor: [contract_dex_storage_stream_cursor_input]!

            """filter the rows returned"""
            where: contract_dex_storage_bool_exp
        ): [contract_dex_storage!]!

        """
        fetch data from the table: "contract_factory_doga_operations"
        """
        contract_factory_doga_operations(
            """distinct select on columns"""
            distinct_on: [contract_factory_doga_operations_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_factory_doga_operations_order_by!]

            """filter the rows returned"""
            where: contract_factory_doga_operations_bool_exp
        ): [contract_factory_doga_operations!]!

        """
        fetch aggregated fields from the table: "contract_factory_doga_operations"
        """
        contract_factory_doga_operations_aggregate(
            """distinct select on columns"""
            distinct_on: [contract_factory_doga_operations_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_factory_doga_operations_order_by!]

            """filter the rows returned"""
            where: contract_factory_doga_operations_bool_exp
        ): contract_factory_doga_operations_aggregate!

        """
        fetch data from the table: "contract_factory_doga_operations" using primary key columns
        """
        contract_factory_doga_operations_by_pk(id: Int!): contract_factory_doga_operations

        """
        fetch data from the table in a streaming manner: "contract_factory_doga_operations"
        """
        contract_factory_doga_operations_stream(
            """maximum number of rows returned in a single batch"""
            batch_size: Int!

            """cursor to stream the results returned by the query"""
            cursor: [contract_factory_doga_operations_stream_cursor_input]!

            """filter the rows returned"""
            where: contract_factory_doga_operations_bool_exp
        ): [contract_factory_doga_operations!]!

        """
        fetch data from the table: "contract_factory_doga_storage"
        """
        contract_factory_doga_storage(
            """distinct select on columns"""
            distinct_on: [contract_factory_doga_storage_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_factory_doga_storage_order_by!]

            """filter the rows returned"""
            where: contract_factory_doga_storage_bool_exp
        ): [contract_factory_doga_storage!]!

        """
        fetch aggregated fields from the table: "contract_factory_doga_storage"
        """
        contract_factory_doga_storage_aggregate(
            """distinct select on columns"""
            distinct_on: [contract_factory_doga_storage_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_factory_doga_storage_order_by!]

            """filter the rows returned"""
            where: contract_factory_doga_storage_bool_exp
        ): contract_factory_doga_storage_aggregate!

        """
        fetch data from the table: "contract_factory_doga_storage" using primary key columns
        """
        contract_factory_doga_storage_by_pk(id: Int!): contract_factory_doga_storage

        """
        fetch data from the table in a streaming manner: "contract_factory_doga_storage"
        """
        contract_factory_doga_storage_stream(
            """maximum number of rows returned in a single batch"""
            batch_size: Int!

            """cursor to stream the results returned by the query"""
            cursor: [contract_factory_doga_storage_stream_cursor_input]!

            """filter the rows returned"""
            where: contract_factory_doga_storage_bool_exp
        ): [contract_factory_doga_storage!]!

        """
        fetch data from the table: "contract_factory_fa12_operations"
        """
        contract_factory_fa12_operations(
            """distinct select on columns"""
            distinct_on: [contract_factory_fa12_operations_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_factory_fa12_operations_order_by!]

            """filter the rows returned"""
            where: contract_factory_fa12_operations_bool_exp
        ): [contract_factory_fa12_operations!]!

        """
        fetch aggregated fields from the table: "contract_factory_fa12_operations"
        """
        contract_factory_fa12_operations_aggregate(
            """distinct select on columns"""
            distinct_on: [contract_factory_fa12_operations_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_factory_fa12_operations_order_by!]

            """filter the rows returned"""
            where: contract_factory_fa12_operations_bool_exp
        ): contract_factory_fa12_operations_aggregate!

        """
        fetch data from the table: "contract_factory_fa12_operations" using primary key columns
        """
        contract_factory_fa12_operations_by_pk(id: Int!): contract_factory_fa12_operations

        """
        fetch data from the table in a streaming manner: "contract_factory_fa12_operations"
        """
        contract_factory_fa12_operations_stream(
            """maximum number of rows returned in a single batch"""
            batch_size: Int!

            """cursor to stream the results returned by the query"""
            cursor: [contract_factory_fa12_operations_stream_cursor_input]!

            """filter the rows returned"""
            where: contract_factory_fa12_operations_bool_exp
        ): [contract_factory_fa12_operations!]!

        """
        fetch data from the table: "contract_factory_fa12_storage"
        """
        contract_factory_fa12_storage(
            """distinct select on columns"""
            distinct_on: [contract_factory_fa12_storage_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_factory_fa12_storage_order_by!]

            """filter the rows returned"""
            where: contract_factory_fa12_storage_bool_exp
        ): [contract_factory_fa12_storage!]!

        """
        fetch aggregated fields from the table: "contract_factory_fa12_storage"
        """
        contract_factory_fa12_storage_aggregate(
            """distinct select on columns"""
            distinct_on: [contract_factory_fa12_storage_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_factory_fa12_storage_order_by!]

            """filter the rows returned"""
            where: contract_factory_fa12_storage_bool_exp
        ): contract_factory_fa12_storage_aggregate!

        """
        fetch data from the table: "contract_factory_fa12_storage" using primary key columns
        """
        contract_factory_fa12_storage_by_pk(id: Int!): contract_factory_fa12_storage

        """
        fetch data from the table in a streaming manner: "contract_factory_fa12_storage"
        """
        contract_factory_fa12_storage_stream(
            """maximum number of rows returned in a single batch"""
            batch_size: Int!

            """cursor to stream the results returned by the query"""
            cursor: [contract_factory_fa12_storage_stream_cursor_input]!

            """filter the rows returned"""
            where: contract_factory_fa12_storage_bool_exp
        ): [contract_factory_fa12_storage!]!

        """
        fetch data from the table: "contract_factory_fa2_operations"
        """
        contract_factory_fa2_operations(
            """distinct select on columns"""
            distinct_on: [contract_factory_fa2_operations_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_factory_fa2_operations_order_by!]

            """filter the rows returned"""
            where: contract_factory_fa2_operations_bool_exp
        ): [contract_factory_fa2_operations!]!

        """
        fetch aggregated fields from the table: "contract_factory_fa2_operations"
        """
        contract_factory_fa2_operations_aggregate(
            """distinct select on columns"""
            distinct_on: [contract_factory_fa2_operations_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_factory_fa2_operations_order_by!]

            """filter the rows returned"""
            where: contract_factory_fa2_operations_bool_exp
        ): contract_factory_fa2_operations_aggregate!

        """
        fetch data from the table: "contract_factory_fa2_operations" using primary key columns
        """
        contract_factory_fa2_operations_by_pk(id: Int!): contract_factory_fa2_operations

        """
        fetch data from the table in a streaming manner: "contract_factory_fa2_operations"
        """
        contract_factory_fa2_operations_stream(
            """maximum number of rows returned in a single batch"""
            batch_size: Int!

            """cursor to stream the results returned by the query"""
            cursor: [contract_factory_fa2_operations_stream_cursor_input]!

            """filter the rows returned"""
            where: contract_factory_fa2_operations_bool_exp
        ): [contract_factory_fa2_operations!]!

        """
        fetch data from the table: "contract_factory_fa2_storage"
        """
        contract_factory_fa2_storage(
            """distinct select on columns"""
            distinct_on: [contract_factory_fa2_storage_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_factory_fa2_storage_order_by!]

            """filter the rows returned"""
            where: contract_factory_fa2_storage_bool_exp
        ): [contract_factory_fa2_storage!]!

        """
        fetch aggregated fields from the table: "contract_factory_fa2_storage"
        """
        contract_factory_fa2_storage_aggregate(
            """distinct select on columns"""
            distinct_on: [contract_factory_fa2_storage_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_factory_fa2_storage_order_by!]

            """filter the rows returned"""
            where: contract_factory_fa2_storage_bool_exp
        ): contract_factory_fa2_storage_aggregate!

        """
        fetch data from the table: "contract_factory_fa2_storage" using primary key columns
        """
        contract_factory_fa2_storage_by_pk(id: Int!): contract_factory_fa2_storage

        """
        fetch data from the table in a streaming manner: "contract_factory_fa2_storage"
        """
        contract_factory_fa2_storage_stream(
            """maximum number of rows returned in a single batch"""
            batch_size: Int!

            """cursor to stream the results returned by the query"""
            cursor: [contract_factory_fa2_storage_stream_cursor_input]!

            """filter the rows returned"""
            where: contract_factory_fa2_storage_bool_exp
        ): [contract_factory_fa2_storage!]!

        """
        fetch data from the table: "contract_farms_v1_operations"
        """
        contract_farms_v1_operations(
            """distinct select on columns"""
            distinct_on: [contract_farms_v1_operations_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_farms_v1_operations_order_by!]

            """filter the rows returned"""
            where: contract_farms_v1_operations_bool_exp
        ): [contract_farms_v1_operations!]!

        """
        fetch aggregated fields from the table: "contract_farms_v1_operations"
        """
        contract_farms_v1_operations_aggregate(
            """distinct select on columns"""
            distinct_on: [contract_farms_v1_operations_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_farms_v1_operations_order_by!]

            """filter the rows returned"""
            where: contract_farms_v1_operations_bool_exp
        ): contract_farms_v1_operations_aggregate!

        """
        fetch data from the table: "contract_farms_v1_operations" using primary key columns
        """
        contract_farms_v1_operations_by_pk(id: Int!): contract_farms_v1_operations

        """
        fetch data from the table in a streaming manner: "contract_farms_v1_operations"
        """
        contract_farms_v1_operations_stream(
            """maximum number of rows returned in a single batch"""
            batch_size: Int!

            """cursor to stream the results returned by the query"""
            cursor: [contract_farms_v1_operations_stream_cursor_input]!

            """filter the rows returned"""
            where: contract_farms_v1_operations_bool_exp
        ): [contract_farms_v1_operations!]!

        """
        fetch data from the table: "contract_farms_v1_storage"
        """
        contract_farms_v1_storage(
            """distinct select on columns"""
            distinct_on: [contract_farms_v1_storage_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_farms_v1_storage_order_by!]

            """filter the rows returned"""
            where: contract_farms_v1_storage_bool_exp
        ): [contract_farms_v1_storage!]!

        """
        fetch aggregated fields from the table: "contract_farms_v1_storage"
        """
        contract_farms_v1_storage_aggregate(
            """distinct select on columns"""
            distinct_on: [contract_farms_v1_storage_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_farms_v1_storage_order_by!]

            """filter the rows returned"""
            where: contract_farms_v1_storage_bool_exp
        ): contract_farms_v1_storage_aggregate!

        """
        fetch data from the table: "contract_farms_v1_storage" using primary key columns
        """
        contract_farms_v1_storage_by_pk(id: Int!): contract_farms_v1_storage

        """
        fetch data from the table in a streaming manner: "contract_farms_v1_storage"
        """
        contract_farms_v1_storage_stream(
            """maximum number of rows returned in a single batch"""
            batch_size: Int!

            """cursor to stream the results returned by the query"""
            cursor: [contract_farms_v1_storage_stream_cursor_input]!

            """filter the rows returned"""
            where: contract_farms_v1_storage_bool_exp
        ): [contract_farms_v1_storage!]!

        """
        fetch data from the table: "contract_farms_v2_allfarms"
        """
        contract_farms_v2_allfarms(
            """distinct select on columns"""
            distinct_on: [contract_farms_v2_allfarms_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_farms_v2_allfarms_order_by!]

            """filter the rows returned"""
            where: contract_farms_v2_allfarms_bool_exp
        ): [contract_farms_v2_allfarms!]!

        """
        fetch aggregated fields from the table: "contract_farms_v2_allfarms"
        """
        contract_farms_v2_allfarms_aggregate(
            """distinct select on columns"""
            distinct_on: [contract_farms_v2_allfarms_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_farms_v2_allfarms_order_by!]

            """filter the rows returned"""
            where: contract_farms_v2_allfarms_bool_exp
        ): contract_farms_v2_allfarms_aggregate!

        """
        fetch data from the table: "contract_farms_v2_allfarms" using primary key columns
        """
        contract_farms_v2_allfarms_by_pk(id: Int!): contract_farms_v2_allfarms

        """
        fetch data from the table in a streaming manner: "contract_farms_v2_allfarms"
        """
        contract_farms_v2_allfarms_stream(
            """maximum number of rows returned in a single batch"""
            batch_size: Int!

            """cursor to stream the results returned by the query"""
            cursor: [contract_farms_v2_allfarms_stream_cursor_input]!

            """filter the rows returned"""
            where: contract_farms_v2_allfarms_bool_exp
        ): [contract_farms_v2_allfarms!]!

        """
        fetch data from the table: "contract_farms_v2_operations"
        """
        contract_farms_v2_operations(
            """distinct select on columns"""
            distinct_on: [contract_farms_v2_operations_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_farms_v2_operations_order_by!]

            """filter the rows returned"""
            where: contract_farms_v2_operations_bool_exp
        ): [contract_farms_v2_operations!]!

        """
        fetch aggregated fields from the table: "contract_farms_v2_operations"
        """
        contract_farms_v2_operations_aggregate(
            """distinct select on columns"""
            distinct_on: [contract_farms_v2_operations_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_farms_v2_operations_order_by!]

            """filter the rows returned"""
            where: contract_farms_v2_operations_bool_exp
        ): contract_farms_v2_operations_aggregate!

        """
        fetch data from the table: "contract_farms_v2_operations" using primary key columns
        """
        contract_farms_v2_operations_by_pk(id: Int!): contract_farms_v2_operations

        """
        fetch data from the table in a streaming manner: "contract_farms_v2_operations"
        """
        contract_farms_v2_operations_stream(
            """maximum number of rows returned in a single batch"""
            batch_size: Int!

            """cursor to stream the results returned by the query"""
            cursor: [contract_farms_v2_operations_stream_cursor_input]!

            """filter the rows returned"""
            where: contract_farms_v2_operations_bool_exp
        ): [contract_farms_v2_operations!]!

        """
        fetch data from the table: "contract_farms_v2_storage"
        """
        contract_farms_v2_storage(
            """distinct select on columns"""
            distinct_on: [contract_farms_v2_storage_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_farms_v2_storage_order_by!]

            """filter the rows returned"""
            where: contract_farms_v2_storage_bool_exp
        ): [contract_farms_v2_storage!]!

        """
        fetch aggregated fields from the table: "contract_farms_v2_storage"
        """
        contract_farms_v2_storage_aggregate(
            """distinct select on columns"""
            distinct_on: [contract_farms_v2_storage_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_farms_v2_storage_order_by!]

            """filter the rows returned"""
            where: contract_farms_v2_storage_bool_exp
        ): contract_farms_v2_storage_aggregate!

        """
        fetch data from the table: "contract_farms_v2_storage" using primary key columns
        """
        contract_farms_v2_storage_by_pk(id: Int!): contract_farms_v2_storage

        """
        fetch data from the table in a streaming manner: "contract_farms_v2_storage"
        """
        contract_farms_v2_storage_stream(
            """maximum number of rows returned in a single batch"""
            batch_size: Int!

            """cursor to stream the results returned by the query"""
            cursor: [contract_farms_v2_storage_stream_cursor_input]!

            """filter the rows returned"""
            where: contract_farms_v2_storage_bool_exp
        ): [contract_farms_v2_storage!]!

        """
        fetch data from the table: "contract_staking_smak_operations"
        """
        contract_staking_smak_operations(
            """distinct select on columns"""
            distinct_on: [contract_staking_smak_operations_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_staking_smak_operations_order_by!]

            """filter the rows returned"""
            where: contract_staking_smak_operations_bool_exp
        ): [contract_staking_smak_operations!]!

        """
        fetch aggregated fields from the table: "contract_staking_smak_operations"
        """
        contract_staking_smak_operations_aggregate(
            """distinct select on columns"""
            distinct_on: [contract_staking_smak_operations_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_staking_smak_operations_order_by!]

            """filter the rows returned"""
            where: contract_staking_smak_operations_bool_exp
        ): contract_staking_smak_operations_aggregate!

        """
        fetch data from the table: "contract_staking_smak_operations" using primary key columns
        """
        contract_staking_smak_operations_by_pk(id: Int!): contract_staking_smak_operations

        """
        fetch data from the table in a streaming manner: "contract_staking_smak_operations"
        """
        contract_staking_smak_operations_stream(
            """maximum number of rows returned in a single batch"""
            batch_size: Int!

            """cursor to stream the results returned by the query"""
            cursor: [contract_staking_smak_operations_stream_cursor_input]!

            """filter the rows returned"""
            where: contract_staking_smak_operations_bool_exp
        ): [contract_staking_smak_operations!]!

        """
        fetch data from the table: "contract_staking_smak_storage"
        """
        contract_staking_smak_storage(
            """distinct select on columns"""
            distinct_on: [contract_staking_smak_storage_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_staking_smak_storage_order_by!]

            """filter the rows returned"""
            where: contract_staking_smak_storage_bool_exp
        ): [contract_staking_smak_storage!]!

        """
        fetch aggregated fields from the table: "contract_staking_smak_storage"
        """
        contract_staking_smak_storage_aggregate(
            """distinct select on columns"""
            distinct_on: [contract_staking_smak_storage_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_staking_smak_storage_order_by!]

            """filter the rows returned"""
            where: contract_staking_smak_storage_bool_exp
        ): contract_staking_smak_storage_aggregate!

        """
        fetch data from the table: "contract_staking_smak_storage" using primary key columns
        """
        contract_staking_smak_storage_by_pk(id: Int!): contract_staking_smak_storage

        """
        fetch data from the table in a streaming manner: "contract_staking_smak_storage"
        """
        contract_staking_smak_storage_stream(
            """maximum number of rows returned in a single batch"""
            batch_size: Int!

            """cursor to stream the results returned by the query"""
            cursor: [contract_staking_smak_storage_stream_cursor_input]!

            """filter the rows returned"""
            where: contract_staking_smak_storage_bool_exp
        ): [contract_staking_smak_storage!]!

        """
        fetch data from the table: "contract_token_anti_operations"
        """
        contract_token_anti_operations(
            """distinct select on columns"""
            distinct_on: [contract_token_anti_operations_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_token_anti_operations_order_by!]

            """filter the rows returned"""
            where: contract_token_anti_operations_bool_exp
        ): [contract_token_anti_operations!]!

        """
        fetch aggregated fields from the table: "contract_token_anti_operations"
        """
        contract_token_anti_operations_aggregate(
            """distinct select on columns"""
            distinct_on: [contract_token_anti_operations_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_token_anti_operations_order_by!]

            """filter the rows returned"""
            where: contract_token_anti_operations_bool_exp
        ): contract_token_anti_operations_aggregate!

        """
        fetch data from the table: "contract_token_anti_operations" using primary key columns
        """
        contract_token_anti_operations_by_pk(id: Int!): contract_token_anti_operations

        """
        fetch data from the table in a streaming manner: "contract_token_anti_operations"
        """
        contract_token_anti_operations_stream(
            """maximum number of rows returned in a single batch"""
            batch_size: Int!

            """cursor to stream the results returned by the query"""
            cursor: [contract_token_anti_operations_stream_cursor_input]!

            """filter the rows returned"""
            where: contract_token_anti_operations_bool_exp
        ): [contract_token_anti_operations!]!

        """
        fetch data from the table: "contract_token_anti_storage"
        """
        contract_token_anti_storage(
            """distinct select on columns"""
            distinct_on: [contract_token_anti_storage_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_token_anti_storage_order_by!]

            """filter the rows returned"""
            where: contract_token_anti_storage_bool_exp
        ): [contract_token_anti_storage!]!

        """
        fetch aggregated fields from the table: "contract_token_anti_storage"
        """
        contract_token_anti_storage_aggregate(
            """distinct select on columns"""
            distinct_on: [contract_token_anti_storage_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_token_anti_storage_order_by!]

            """filter the rows returned"""
            where: contract_token_anti_storage_bool_exp
        ): contract_token_anti_storage_aggregate!

        """
        fetch data from the table: "contract_token_anti_storage" using primary key columns
        """
        contract_token_anti_storage_by_pk(id: Int!): contract_token_anti_storage

        """
        fetch data from the table in a streaming manner: "contract_token_anti_storage"
        """
        contract_token_anti_storage_stream(
            """maximum number of rows returned in a single batch"""
            batch_size: Int!

            """cursor to stream the results returned by the query"""
            cursor: [contract_token_anti_storage_stream_cursor_input]!

            """filter the rows returned"""
            where: contract_token_anti_storage_bool_exp
        ): [contract_token_anti_storage!]!

        """
        fetch data from the table: "contract_token_smak_operations"
        """
        contract_token_smak_operations(
            """distinct select on columns"""
            distinct_on: [contract_token_smak_operations_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_token_smak_operations_order_by!]

            """filter the rows returned"""
            where: contract_token_smak_operations_bool_exp
        ): [contract_token_smak_operations!]!

        """
        fetch aggregated fields from the table: "contract_token_smak_operations"
        """
        contract_token_smak_operations_aggregate(
            """distinct select on columns"""
            distinct_on: [contract_token_smak_operations_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_token_smak_operations_order_by!]

            """filter the rows returned"""
            where: contract_token_smak_operations_bool_exp
        ): contract_token_smak_operations_aggregate!

        """
        fetch data from the table: "contract_token_smak_operations" using primary key columns
        """
        contract_token_smak_operations_by_pk(id: Int!): contract_token_smak_operations

        """
        fetch data from the table in a streaming manner: "contract_token_smak_operations"
        """
        contract_token_smak_operations_stream(
            """maximum number of rows returned in a single batch"""
            batch_size: Int!

            """cursor to stream the results returned by the query"""
            cursor: [contract_token_smak_operations_stream_cursor_input]!

            """filter the rows returned"""
            where: contract_token_smak_operations_bool_exp
        ): [contract_token_smak_operations!]!

        """
        fetch data from the table: "contract_token_smak_storage"
        """
        contract_token_smak_storage(
            """distinct select on columns"""
            distinct_on: [contract_token_smak_storage_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_token_smak_storage_order_by!]

            """filter the rows returned"""
            where: contract_token_smak_storage_bool_exp
        ): [contract_token_smak_storage!]!

        """
        fetch aggregated fields from the table: "contract_token_smak_storage"
        """
        contract_token_smak_storage_aggregate(
            """distinct select on columns"""
            distinct_on: [contract_token_smak_storage_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [contract_token_smak_storage_order_by!]

            """filter the rows returned"""
            where: contract_token_smak_storage_bool_exp
        ): contract_token_smak_storage_aggregate!

        """
        fetch data from the table: "contract_token_smak_storage" using primary key columns
        """
        contract_token_smak_storage_by_pk(id: Int!): contract_token_smak_storage

        """
        fetch data from the table in a streaming manner: "contract_token_smak_storage"
        """
        contract_token_smak_storage_stream(
            """maximum number of rows returned in a single batch"""
            batch_size: Int!

            """cursor to stream the results returned by the query"""
            cursor: [contract_token_smak_storage_stream_cursor_input]!

            """filter the rows returned"""
            where: contract_token_smak_storage_bool_exp
        ): [contract_token_smak_storage!]!

        """
        fetch data from the table: "indexer"
        """
        indexer(
            """distinct select on columns"""
            distinct_on: [indexer_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [indexer_order_by!]

            """filter the rows returned"""
            where: indexer_bool_exp
        ): [indexer!]!

        """
        fetch aggregated fields from the table: "indexer"
        """
        indexer_aggregate(
            """distinct select on columns"""
            distinct_on: [indexer_select_column!]

            """limit the number of rows returned"""
            limit: Int

            """skip the first n rows. Use only with order_by"""
            offset: Int

            """sort the rows by one or more columns"""
            order_by: [indexer_order_by!]

            """filter the rows returned"""
            where: indexer_bool_exp
        ): indexer_aggregate!

        """fetch data from the table: "indexer" using primary key columns"""
        indexer_by_pk(id: Int!): indexer

        """
        fetch data from the table in a streaming manner: "indexer"
        """
        indexer_stream(
            """maximum number of rows returned in a single batch"""
            batch_size: Int!

            """cursor to stream the results returned by the query"""
            cursor: [indexer_stream_cursor_input]!

            """filter the rows returned"""
            where: indexer_bool_exp
        ): [indexer!]!
        }
    '''

    # Create a Tartiflette engine with the defined schema and resolvers
    print("Starting the GraphQL Server...")
    engine = Engine(sdl=sdl)
    app = TartifletteApp(engine=engine, sdl=sdl, path="/")
    return app