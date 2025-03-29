from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DataType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATA_TYPE_UNSPECIFIED: _ClassVar[DataType]
    DATA_TYPE_BOOLEAN: _ClassVar[DataType]
    DATA_TYPE_INT: _ClassVar[DataType]
    DATA_TYPE_BIGINT: _ClassVar[DataType]
    DATA_TYPE_FLOAT: _ClassVar[DataType]
    DATA_TYPE_DOUBLE: _ClassVar[DataType]
    DATA_TYPE_TEXT: _ClassVar[DataType]
    DATA_TYPE_BLOB: _ClassVar[DataType]
    DATA_TYPE_DATE: _ClassVar[DataType]
    DATA_TYPE_TIME: _ClassVar[DataType]
    DATA_TYPE_TIMESTAMP: _ClassVar[DataType]
    DATA_TYPE_TIMESTAMPTZ: _ClassVar[DataType]

class ClusteringOrder(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CLUSTERING_ORDER_UNSPECIFIED: _ClassVar[ClusteringOrder]
    CLUSTERING_ORDER_ASC: _ClassVar[ClusteringOrder]
    CLUSTERING_ORDER_DESC: _ClassVar[ClusteringOrder]

class Privilege(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRIVILEGE_UNSPECIFIED: _ClassVar[Privilege]
    PRIVILEGE_SELECT: _ClassVar[Privilege]
    PRIVILEGE_INSERT: _ClassVar[Privilege]
    PRIVILEGE_UPDATE: _ClassVar[Privilege]
    PRIVILEGE_DELETE: _ClassVar[Privilege]
    PRIVILEGE_CREATE: _ClassVar[Privilege]
    PRIVILEGE_DROP: _ClassVar[Privilege]
    PRIVILEGE_TRUNCATE: _ClassVar[Privilege]
    PRIVILEGE_ALTER: _ClassVar[Privilege]
    PRIVILEGE_GRANT: _ClassVar[Privilege]

class PolicyState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    POLICY_STATE_UNSPECIFIED: _ClassVar[PolicyState]
    POLICY_STATE_ENABLED: _ClassVar[PolicyState]
    POLICY_STATE_DISABLED: _ClassVar[PolicyState]
DATA_TYPE_UNSPECIFIED: DataType
DATA_TYPE_BOOLEAN: DataType
DATA_TYPE_INT: DataType
DATA_TYPE_BIGINT: DataType
DATA_TYPE_FLOAT: DataType
DATA_TYPE_DOUBLE: DataType
DATA_TYPE_TEXT: DataType
DATA_TYPE_BLOB: DataType
DATA_TYPE_DATE: DataType
DATA_TYPE_TIME: DataType
DATA_TYPE_TIMESTAMP: DataType
DATA_TYPE_TIMESTAMPTZ: DataType
CLUSTERING_ORDER_UNSPECIFIED: ClusteringOrder
CLUSTERING_ORDER_ASC: ClusteringOrder
CLUSTERING_ORDER_DESC: ClusteringOrder
PRIVILEGE_UNSPECIFIED: Privilege
PRIVILEGE_SELECT: Privilege
PRIVILEGE_INSERT: Privilege
PRIVILEGE_UPDATE: Privilege
PRIVILEGE_DELETE: Privilege
PRIVILEGE_CREATE: Privilege
PRIVILEGE_DROP: Privilege
PRIVILEGE_TRUNCATE: Privilege
PRIVILEGE_ALTER: Privilege
PRIVILEGE_GRANT: Privilege
POLICY_STATE_UNSPECIFIED: PolicyState
POLICY_STATE_ENABLED: PolicyState
POLICY_STATE_DISABLED: PolicyState

class Value(_message.Message):
    __slots__ = ("boolean_value", "int_value", "bigint_value", "float_value", "double_value", "text_value", "blob_value", "date_value", "time_value", "timestamp_value", "timestamptz_value")
    BOOLEAN_VALUE_FIELD_NUMBER: _ClassVar[int]
    INT_VALUE_FIELD_NUMBER: _ClassVar[int]
    BIGINT_VALUE_FIELD_NUMBER: _ClassVar[int]
    FLOAT_VALUE_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    TEXT_VALUE_FIELD_NUMBER: _ClassVar[int]
    BLOB_VALUE_FIELD_NUMBER: _ClassVar[int]
    DATE_VALUE_FIELD_NUMBER: _ClassVar[int]
    TIME_VALUE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_VALUE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMPTZ_VALUE_FIELD_NUMBER: _ClassVar[int]
    boolean_value: bool
    int_value: int
    bigint_value: int
    float_value: float
    double_value: float
    text_value: str
    blob_value: bytes
    date_value: int
    time_value: int
    timestamp_value: int
    timestamptz_value: int
    def __init__(self, boolean_value: bool = ..., int_value: _Optional[int] = ..., bigint_value: _Optional[int] = ..., float_value: _Optional[float] = ..., double_value: _Optional[float] = ..., text_value: _Optional[str] = ..., blob_value: _Optional[bytes] = ..., date_value: _Optional[int] = ..., time_value: _Optional[int] = ..., timestamp_value: _Optional[int] = ..., timestamptz_value: _Optional[int] = ...) -> None: ...

class ColumnDefinitions(_message.Message):
    __slots__ = ("column_definitions",)
    COLUMN_DEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    column_definitions: _containers.RepeatedCompositeFieldContainer[ColumnDefinition]
    def __init__(self, column_definitions: _Optional[_Iterable[_Union[ColumnDefinition, _Mapping]]] = ...) -> None: ...

class ColumnDefinition(_message.Message):
    __slots__ = ("namespace_name", "table_name", "column_name", "data_type")
    NAMESPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    namespace_name: str
    table_name: str
    column_name: str
    data_type: DataType
    def __init__(self, namespace_name: _Optional[str] = ..., table_name: _Optional[str] = ..., column_name: _Optional[str] = ..., data_type: _Optional[_Union[DataType, str]] = ...) -> None: ...

class ResultSet(_message.Message):
    __slots__ = ("column_definitions", "records")
    COLUMN_DEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    RECORDS_FIELD_NUMBER: _ClassVar[int]
    column_definitions: ColumnDefinitions
    records: _containers.RepeatedCompositeFieldContainer[Record]
    def __init__(self, column_definitions: _Optional[_Union[ColumnDefinitions, _Mapping]] = ..., records: _Optional[_Iterable[_Union[Record, _Mapping]]] = ...) -> None: ...

class Record(_message.Message):
    __slots__ = ("columns",)
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    columns: _containers.RepeatedCompositeFieldContainer[Column]
    def __init__(self, columns: _Optional[_Iterable[_Union[Column, _Mapping]]] = ...) -> None: ...

class Column(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: Value
    def __init__(self, name: _Optional[str] = ..., value: _Optional[_Union[Value, _Mapping]] = ...) -> None: ...

class RequestHeader(_message.Message):
    __slots__ = ("hop_limit", "auth_token")
    HOP_LIMIT_FIELD_NUMBER: _ClassVar[int]
    AUTH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    hop_limit: int
    auth_token: str
    def __init__(self, hop_limit: _Optional[int] = ..., auth_token: _Optional[str] = ...) -> None: ...

class BeginRequest(_message.Message):
    __slots__ = ("request_header", "transaction_id")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    transaction_id: str
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., transaction_id: _Optional[str] = ...) -> None: ...

class BeginResponse(_message.Message):
    __slots__ = ("transaction_id",)
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    transaction_id: str
    def __init__(self, transaction_id: _Optional[str] = ...) -> None: ...

class ExecuteRequest(_message.Message):
    __slots__ = ("request_header", "transaction_id", "sql", "positional_values", "named_values", "default_namespace_name")
    class PositionalValues(_message.Message):
        __slots__ = ("positional_values",)
        POSITIONAL_VALUES_FIELD_NUMBER: _ClassVar[int]
        positional_values: _containers.RepeatedCompositeFieldContainer[Value]
        def __init__(self, positional_values: _Optional[_Iterable[_Union[Value, _Mapping]]] = ...) -> None: ...
    class NamedValues(_message.Message):
        __slots__ = ("named_values",)
        class NamedValuesEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: Value
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Value, _Mapping]] = ...) -> None: ...
        NAMED_VALUES_FIELD_NUMBER: _ClassVar[int]
        named_values: _containers.MessageMap[str, Value]
        def __init__(self, named_values: _Optional[_Mapping[str, Value]] = ...) -> None: ...
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    SQL_FIELD_NUMBER: _ClassVar[int]
    POSITIONAL_VALUES_FIELD_NUMBER: _ClassVar[int]
    NAMED_VALUES_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_NAMESPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    transaction_id: str
    sql: str
    positional_values: ExecuteRequest.PositionalValues
    named_values: ExecuteRequest.NamedValues
    default_namespace_name: str
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., transaction_id: _Optional[str] = ..., sql: _Optional[str] = ..., positional_values: _Optional[_Union[ExecuteRequest.PositionalValues, _Mapping]] = ..., named_values: _Optional[_Union[ExecuteRequest.NamedValues, _Mapping]] = ..., default_namespace_name: _Optional[str] = ...) -> None: ...

class ExecuteResponse(_message.Message):
    __slots__ = ("result_set",)
    RESULT_SET_FIELD_NUMBER: _ClassVar[int]
    result_set: ResultSet
    def __init__(self, result_set: _Optional[_Union[ResultSet, _Mapping]] = ...) -> None: ...

class CommitRequest(_message.Message):
    __slots__ = ("request_header", "transaction_id")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    transaction_id: str
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., transaction_id: _Optional[str] = ...) -> None: ...

class CommitResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RollbackRequest(_message.Message):
    __slots__ = ("request_header", "transaction_id")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    transaction_id: str
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., transaction_id: _Optional[str] = ...) -> None: ...

class RollbackResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class JoinRequest(_message.Message):
    __slots__ = ("request_header", "transaction_id")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    transaction_id: str
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., transaction_id: _Optional[str] = ...) -> None: ...

class JoinResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PrepareRequest(_message.Message):
    __slots__ = ("request_header", "transaction_id")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    transaction_id: str
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., transaction_id: _Optional[str] = ...) -> None: ...

class PrepareResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ValidateRequest(_message.Message):
    __slots__ = ("request_header", "transaction_id")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    transaction_id: str
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., transaction_id: _Optional[str] = ...) -> None: ...

class ValidateResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class NamespaceMetadata(_message.Message):
    __slots__ = ("namespace_name",)
    NAMESPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    namespace_name: str
    def __init__(self, namespace_name: _Optional[str] = ...) -> None: ...

class TableMetadata(_message.Message):
    __slots__ = ("table_name", "partition_key_column_names", "clustering_key_column_names", "clustering_orders", "columns", "indexes")
    class ClusteringOrdersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ClusteringOrder
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ClusteringOrder, str]] = ...) -> None: ...
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    PARTITION_KEY_COLUMN_NAMES_FIELD_NUMBER: _ClassVar[int]
    CLUSTERING_KEY_COLUMN_NAMES_FIELD_NUMBER: _ClassVar[int]
    CLUSTERING_ORDERS_FIELD_NUMBER: _ClassVar[int]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    INDEXES_FIELD_NUMBER: _ClassVar[int]
    table_name: str
    partition_key_column_names: _containers.RepeatedScalarFieldContainer[str]
    clustering_key_column_names: _containers.RepeatedScalarFieldContainer[str]
    clustering_orders: _containers.ScalarMap[str, ClusteringOrder]
    columns: _containers.RepeatedCompositeFieldContainer[ColumnMetadata]
    indexes: _containers.RepeatedCompositeFieldContainer[IndexMetadata]
    def __init__(self, table_name: _Optional[str] = ..., partition_key_column_names: _Optional[_Iterable[str]] = ..., clustering_key_column_names: _Optional[_Iterable[str]] = ..., clustering_orders: _Optional[_Mapping[str, ClusteringOrder]] = ..., columns: _Optional[_Iterable[_Union[ColumnMetadata, _Mapping]]] = ..., indexes: _Optional[_Iterable[_Union[IndexMetadata, _Mapping]]] = ...) -> None: ...

class ColumnMetadata(_message.Message):
    __slots__ = ("column_name", "data_type", "encrypted")
    COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_FIELD_NUMBER: _ClassVar[int]
    column_name: str
    data_type: DataType
    encrypted: bool
    def __init__(self, column_name: _Optional[str] = ..., data_type: _Optional[_Union[DataType, str]] = ..., encrypted: bool = ...) -> None: ...

class IndexMetadata(_message.Message):
    __slots__ = ("column_name",)
    COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
    column_name: str
    def __init__(self, column_name: _Optional[str] = ...) -> None: ...

class ListNamespaceMetadataRequest(_message.Message):
    __slots__ = ("request_header",)
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ...) -> None: ...

class ListNamespaceMetadataResponse(_message.Message):
    __slots__ = ("namespace_metadata",)
    NAMESPACE_METADATA_FIELD_NUMBER: _ClassVar[int]
    namespace_metadata: _containers.RepeatedCompositeFieldContainer[NamespaceMetadata]
    def __init__(self, namespace_metadata: _Optional[_Iterable[_Union[NamespaceMetadata, _Mapping]]] = ...) -> None: ...

class GetNamespaceMetadataRequest(_message.Message):
    __slots__ = ("request_header", "namespace_name")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    namespace_name: str
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., namespace_name: _Optional[str] = ...) -> None: ...

class GetNamespaceMetadataResponse(_message.Message):
    __slots__ = ("namespace_metadata",)
    NAMESPACE_METADATA_FIELD_NUMBER: _ClassVar[int]
    namespace_metadata: NamespaceMetadata
    def __init__(self, namespace_metadata: _Optional[_Union[NamespaceMetadata, _Mapping]] = ...) -> None: ...

class ListTableMetadataInNamespaceRequest(_message.Message):
    __slots__ = ("request_header", "namespace_name")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    namespace_name: str
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., namespace_name: _Optional[str] = ...) -> None: ...

class ListTableMetadataInNamespaceResponse(_message.Message):
    __slots__ = ("table_metadata",)
    TABLE_METADATA_FIELD_NUMBER: _ClassVar[int]
    table_metadata: _containers.RepeatedCompositeFieldContainer[TableMetadata]
    def __init__(self, table_metadata: _Optional[_Iterable[_Union[TableMetadata, _Mapping]]] = ...) -> None: ...

class GetTableMetadataRequest(_message.Message):
    __slots__ = ("request_header", "namespace_name", "table_name")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    namespace_name: str
    table_name: str
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., namespace_name: _Optional[str] = ..., table_name: _Optional[str] = ...) -> None: ...

class GetTableMetadataResponse(_message.Message):
    __slots__ = ("table_metadata",)
    TABLE_METADATA_FIELD_NUMBER: _ClassVar[int]
    table_metadata: TableMetadata
    def __init__(self, table_metadata: _Optional[_Union[TableMetadata, _Mapping]] = ...) -> None: ...

class UserMetadata(_message.Message):
    __slots__ = ("username", "superuser")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    SUPERUSER_FIELD_NUMBER: _ClassVar[int]
    username: str
    superuser: bool
    def __init__(self, username: _Optional[str] = ..., superuser: bool = ...) -> None: ...

class GetUserMetadataRequest(_message.Message):
    __slots__ = ("request_header", "username")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    username: str
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., username: _Optional[str] = ...) -> None: ...

class GetUserMetadataResponse(_message.Message):
    __slots__ = ("user_metadata",)
    USER_METADATA_FIELD_NUMBER: _ClassVar[int]
    user_metadata: UserMetadata
    def __init__(self, user_metadata: _Optional[_Union[UserMetadata, _Mapping]] = ...) -> None: ...

class ListUserMetadataRequest(_message.Message):
    __slots__ = ("request_header",)
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ...) -> None: ...

class ListUserMetadataResponse(_message.Message):
    __slots__ = ("user_metadata",)
    USER_METADATA_FIELD_NUMBER: _ClassVar[int]
    user_metadata: _containers.RepeatedCompositeFieldContainer[UserMetadata]
    def __init__(self, user_metadata: _Optional[_Iterable[_Union[UserMetadata, _Mapping]]] = ...) -> None: ...

class GetCurrentUserMetadataRequest(_message.Message):
    __slots__ = ("request_header",)
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ...) -> None: ...

class GetCurrentUserMetadataResponse(_message.Message):
    __slots__ = ("user_metadata",)
    USER_METADATA_FIELD_NUMBER: _ClassVar[int]
    user_metadata: UserMetadata
    def __init__(self, user_metadata: _Optional[_Union[UserMetadata, _Mapping]] = ...) -> None: ...

class GetPrivilegesRequest(_message.Message):
    __slots__ = ("request_header", "namespace_name", "table_name", "username")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    namespace_name: str
    table_name: str
    username: str
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., namespace_name: _Optional[str] = ..., table_name: _Optional[str] = ..., username: _Optional[str] = ...) -> None: ...

class GetPrivilegesResponse(_message.Message):
    __slots__ = ("privileges",)
    PRIVILEGES_FIELD_NUMBER: _ClassVar[int]
    privileges: _containers.RepeatedScalarFieldContainer[Privilege]
    def __init__(self, privileges: _Optional[_Iterable[_Union[Privilege, str]]] = ...) -> None: ...

class GetPolicyMetadataRequest(_message.Message):
    __slots__ = ("request_header", "policy_name")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    policy_name: str
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., policy_name: _Optional[str] = ...) -> None: ...

class GetPolicyMetadataResponse(_message.Message):
    __slots__ = ("policy_metadata",)
    POLICY_METADATA_FIELD_NUMBER: _ClassVar[int]
    policy_metadata: PolicyMetadata
    def __init__(self, policy_metadata: _Optional[_Union[PolicyMetadata, _Mapping]] = ...) -> None: ...

class ListPolicyMetadataRequest(_message.Message):
    __slots__ = ("request_header",)
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ...) -> None: ...

class ListPolicyMetadataResponse(_message.Message):
    __slots__ = ("policy_metadata",)
    POLICY_METADATA_FIELD_NUMBER: _ClassVar[int]
    policy_metadata: _containers.RepeatedCompositeFieldContainer[PolicyMetadata]
    def __init__(self, policy_metadata: _Optional[_Iterable[_Union[PolicyMetadata, _Mapping]]] = ...) -> None: ...

class GetLevelMetadataRequest(_message.Message):
    __slots__ = ("request_header", "policy_name", "level_short_name")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    LEVEL_SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    policy_name: str
    level_short_name: str
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., policy_name: _Optional[str] = ..., level_short_name: _Optional[str] = ...) -> None: ...

class GetLevelMetadataResponse(_message.Message):
    __slots__ = ("level_metadata",)
    LEVEL_METADATA_FIELD_NUMBER: _ClassVar[int]
    level_metadata: LevelMetadata
    def __init__(self, level_metadata: _Optional[_Union[LevelMetadata, _Mapping]] = ...) -> None: ...

class ListLevelMetadataRequest(_message.Message):
    __slots__ = ("request_header", "policy_name")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    policy_name: str
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., policy_name: _Optional[str] = ...) -> None: ...

class ListLevelMetadataResponse(_message.Message):
    __slots__ = ("level_metadata",)
    LEVEL_METADATA_FIELD_NUMBER: _ClassVar[int]
    level_metadata: _containers.RepeatedCompositeFieldContainer[LevelMetadata]
    def __init__(self, level_metadata: _Optional[_Iterable[_Union[LevelMetadata, _Mapping]]] = ...) -> None: ...

class GetCompartmentMetadataRequest(_message.Message):
    __slots__ = ("request_header", "policy_name", "compartment_short_name")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    COMPARTMENT_SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    policy_name: str
    compartment_short_name: str
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., policy_name: _Optional[str] = ..., compartment_short_name: _Optional[str] = ...) -> None: ...

class GetCompartmentMetadataResponse(_message.Message):
    __slots__ = ("compartment_metadata",)
    COMPARTMENT_METADATA_FIELD_NUMBER: _ClassVar[int]
    compartment_metadata: CompartmentMetadata
    def __init__(self, compartment_metadata: _Optional[_Union[CompartmentMetadata, _Mapping]] = ...) -> None: ...

class ListCompartmentMetadataRequest(_message.Message):
    __slots__ = ("request_header", "policy_name")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    policy_name: str
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., policy_name: _Optional[str] = ...) -> None: ...

class ListCompartmentMetadataResponse(_message.Message):
    __slots__ = ("compartment_metadata",)
    COMPARTMENT_METADATA_FIELD_NUMBER: _ClassVar[int]
    compartment_metadata: _containers.RepeatedCompositeFieldContainer[CompartmentMetadata]
    def __init__(self, compartment_metadata: _Optional[_Iterable[_Union[CompartmentMetadata, _Mapping]]] = ...) -> None: ...

class GetGroupMetadataRequest(_message.Message):
    __slots__ = ("request_header", "policy_name", "group_short_name")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    GROUP_SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    policy_name: str
    group_short_name: str
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., policy_name: _Optional[str] = ..., group_short_name: _Optional[str] = ...) -> None: ...

class GetGroupMetadataResponse(_message.Message):
    __slots__ = ("group_metadata",)
    GROUP_METADATA_FIELD_NUMBER: _ClassVar[int]
    group_metadata: GroupMetadata
    def __init__(self, group_metadata: _Optional[_Union[GroupMetadata, _Mapping]] = ...) -> None: ...

class ListGroupMetadataRequest(_message.Message):
    __slots__ = ("request_header", "policy_name")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    policy_name: str
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., policy_name: _Optional[str] = ...) -> None: ...

class ListGroupMetadataResponse(_message.Message):
    __slots__ = ("group_metadata",)
    GROUP_METADATA_FIELD_NUMBER: _ClassVar[int]
    group_metadata: _containers.RepeatedCompositeFieldContainer[GroupMetadata]
    def __init__(self, group_metadata: _Optional[_Iterable[_Union[GroupMetadata, _Mapping]]] = ...) -> None: ...

class GetUserTagInfoRequest(_message.Message):
    __slots__ = ("request_header", "policy_name", "username")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    policy_name: str
    username: str
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., policy_name: _Optional[str] = ..., username: _Optional[str] = ...) -> None: ...

class GetUserTagInfoResponse(_message.Message):
    __slots__ = ("user_tag_info",)
    USER_TAG_INFO_FIELD_NUMBER: _ClassVar[int]
    user_tag_info: UserTagInfo
    def __init__(self, user_tag_info: _Optional[_Union[UserTagInfo, _Mapping]] = ...) -> None: ...

class GetNamespacePolicyMetadataRequest(_message.Message):
    __slots__ = ("request_header", "namespace_policy_name")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    namespace_policy_name: str
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., namespace_policy_name: _Optional[str] = ...) -> None: ...

class GetNamespacePolicyMetadataResponse(_message.Message):
    __slots__ = ("namespace_policy_metadata",)
    NAMESPACE_POLICY_METADATA_FIELD_NUMBER: _ClassVar[int]
    namespace_policy_metadata: NamespacePolicyMetadata
    def __init__(self, namespace_policy_metadata: _Optional[_Union[NamespacePolicyMetadata, _Mapping]] = ...) -> None: ...

class ListNamespacePolicyMetadataRequest(_message.Message):
    __slots__ = ("request_header",)
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ...) -> None: ...

class ListNamespacePolicyMetadataResponse(_message.Message):
    __slots__ = ("namespace_policy_metadata",)
    NAMESPACE_POLICY_METADATA_FIELD_NUMBER: _ClassVar[int]
    namespace_policy_metadata: _containers.RepeatedCompositeFieldContainer[NamespacePolicyMetadata]
    def __init__(self, namespace_policy_metadata: _Optional[_Iterable[_Union[NamespacePolicyMetadata, _Mapping]]] = ...) -> None: ...

class GetTablePolicyMetadataRequest(_message.Message):
    __slots__ = ("request_header", "table_policy_name")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    TABLE_POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    table_policy_name: str
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., table_policy_name: _Optional[str] = ...) -> None: ...

class GetTablePolicyMetadataResponse(_message.Message):
    __slots__ = ("table_policy_metadata",)
    TABLE_POLICY_METADATA_FIELD_NUMBER: _ClassVar[int]
    table_policy_metadata: TablePolicyMetadata
    def __init__(self, table_policy_metadata: _Optional[_Union[TablePolicyMetadata, _Mapping]] = ...) -> None: ...

class ListTablePolicyMetadataRequest(_message.Message):
    __slots__ = ("request_header",)
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ...) -> None: ...

class ListTablePolicyMetadataResponse(_message.Message):
    __slots__ = ("table_policy_metadata",)
    TABLE_POLICY_METADATA_FIELD_NUMBER: _ClassVar[int]
    table_policy_metadata: _containers.RepeatedCompositeFieldContainer[TablePolicyMetadata]
    def __init__(self, table_policy_metadata: _Optional[_Iterable[_Union[TablePolicyMetadata, _Mapping]]] = ...) -> None: ...

class PolicyMetadata(_message.Message):
    __slots__ = ("name", "data_tag_column_name", "state")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_TAG_COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    data_tag_column_name: str
    state: PolicyState
    def __init__(self, name: _Optional[str] = ..., data_tag_column_name: _Optional[str] = ..., state: _Optional[_Union[PolicyState, str]] = ...) -> None: ...

class LevelMetadata(_message.Message):
    __slots__ = ("policy_name", "short_name", "long_name", "level_number")
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
    LONG_NAME_FIELD_NUMBER: _ClassVar[int]
    LEVEL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    policy_name: str
    short_name: str
    long_name: str
    level_number: int
    def __init__(self, policy_name: _Optional[str] = ..., short_name: _Optional[str] = ..., long_name: _Optional[str] = ..., level_number: _Optional[int] = ...) -> None: ...

class CompartmentMetadata(_message.Message):
    __slots__ = ("policy_name", "short_name", "long_name")
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
    LONG_NAME_FIELD_NUMBER: _ClassVar[int]
    policy_name: str
    short_name: str
    long_name: str
    def __init__(self, policy_name: _Optional[str] = ..., short_name: _Optional[str] = ..., long_name: _Optional[str] = ...) -> None: ...

class GroupMetadata(_message.Message):
    __slots__ = ("policy_name", "short_name", "long_name", "parent_group_short_name")
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
    LONG_NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_GROUP_SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
    policy_name: str
    short_name: str
    long_name: str
    parent_group_short_name: str
    def __init__(self, policy_name: _Optional[str] = ..., short_name: _Optional[str] = ..., long_name: _Optional[str] = ..., parent_group_short_name: _Optional[str] = ...) -> None: ...

class UserTagInfo(_message.Message):
    __slots__ = ("policy_name", "username", "level_info", "compartment_info", "group_info")
    class LevelInfo(_message.Message):
        __slots__ = ("level_short_name", "default_level_short_name", "row_level_short_name")
        LEVEL_SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_LEVEL_SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
        ROW_LEVEL_SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
        level_short_name: str
        default_level_short_name: str
        row_level_short_name: str
        def __init__(self, level_short_name: _Optional[str] = ..., default_level_short_name: _Optional[str] = ..., row_level_short_name: _Optional[str] = ...) -> None: ...
    class CompartmentInfo(_message.Message):
        __slots__ = ("read_compartment_short_names", "write_compartment_short_names", "default_read_compartment_short_names", "default_write_compartment_short_names", "row_compartment_short_names")
        READ_COMPARTMENT_SHORT_NAMES_FIELD_NUMBER: _ClassVar[int]
        WRITE_COMPARTMENT_SHORT_NAMES_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_READ_COMPARTMENT_SHORT_NAMES_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_WRITE_COMPARTMENT_SHORT_NAMES_FIELD_NUMBER: _ClassVar[int]
        ROW_COMPARTMENT_SHORT_NAMES_FIELD_NUMBER: _ClassVar[int]
        read_compartment_short_names: _containers.RepeatedScalarFieldContainer[str]
        write_compartment_short_names: _containers.RepeatedScalarFieldContainer[str]
        default_read_compartment_short_names: _containers.RepeatedScalarFieldContainer[str]
        default_write_compartment_short_names: _containers.RepeatedScalarFieldContainer[str]
        row_compartment_short_names: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, read_compartment_short_names: _Optional[_Iterable[str]] = ..., write_compartment_short_names: _Optional[_Iterable[str]] = ..., default_read_compartment_short_names: _Optional[_Iterable[str]] = ..., default_write_compartment_short_names: _Optional[_Iterable[str]] = ..., row_compartment_short_names: _Optional[_Iterable[str]] = ...) -> None: ...
    class GroupInfo(_message.Message):
        __slots__ = ("read_group_short_names", "write_group_short_names", "default_read_group_short_names", "default_write_group_short_names", "row_group_short_names")
        READ_GROUP_SHORT_NAMES_FIELD_NUMBER: _ClassVar[int]
        WRITE_GROUP_SHORT_NAMES_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_READ_GROUP_SHORT_NAMES_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_WRITE_GROUP_SHORT_NAMES_FIELD_NUMBER: _ClassVar[int]
        ROW_GROUP_SHORT_NAMES_FIELD_NUMBER: _ClassVar[int]
        read_group_short_names: _containers.RepeatedScalarFieldContainer[str]
        write_group_short_names: _containers.RepeatedScalarFieldContainer[str]
        default_read_group_short_names: _containers.RepeatedScalarFieldContainer[str]
        default_write_group_short_names: _containers.RepeatedScalarFieldContainer[str]
        row_group_short_names: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, read_group_short_names: _Optional[_Iterable[str]] = ..., write_group_short_names: _Optional[_Iterable[str]] = ..., default_read_group_short_names: _Optional[_Iterable[str]] = ..., default_write_group_short_names: _Optional[_Iterable[str]] = ..., row_group_short_names: _Optional[_Iterable[str]] = ...) -> None: ...
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    LEVEL_INFO_FIELD_NUMBER: _ClassVar[int]
    COMPARTMENT_INFO_FIELD_NUMBER: _ClassVar[int]
    GROUP_INFO_FIELD_NUMBER: _ClassVar[int]
    policy_name: str
    username: str
    level_info: UserTagInfo.LevelInfo
    compartment_info: UserTagInfo.CompartmentInfo
    group_info: UserTagInfo.GroupInfo
    def __init__(self, policy_name: _Optional[str] = ..., username: _Optional[str] = ..., level_info: _Optional[_Union[UserTagInfo.LevelInfo, _Mapping]] = ..., compartment_info: _Optional[_Union[UserTagInfo.CompartmentInfo, _Mapping]] = ..., group_info: _Optional[_Union[UserTagInfo.GroupInfo, _Mapping]] = ...) -> None: ...

class NamespacePolicyMetadata(_message.Message):
    __slots__ = ("name", "policy_name", "namespace_name", "state")
    NAME_FIELD_NUMBER: _ClassVar[int]
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    policy_name: str
    namespace_name: str
    state: PolicyState
    def __init__(self, name: _Optional[str] = ..., policy_name: _Optional[str] = ..., namespace_name: _Optional[str] = ..., state: _Optional[_Union[PolicyState, str]] = ...) -> None: ...

class TablePolicyMetadata(_message.Message):
    __slots__ = ("name", "policy_name", "namespace_name", "table_name", "state")
    NAME_FIELD_NUMBER: _ClassVar[int]
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    policy_name: str
    namespace_name: str
    table_name: str
    state: PolicyState
    def __init__(self, name: _Optional[str] = ..., policy_name: _Optional[str] = ..., namespace_name: _Optional[str] = ..., table_name: _Optional[str] = ..., state: _Optional[_Union[PolicyState, str]] = ...) -> None: ...
