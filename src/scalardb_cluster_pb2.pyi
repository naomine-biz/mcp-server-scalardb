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

class UserOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    USER_OPTION_UNSPECIFIED: _ClassVar[UserOption]
    USER_OPTION_SUPERUSER: _ClassVar[UserOption]
    USER_OPTION_NO_SUPERUSER: _ClassVar[UserOption]

class Privilege(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRIVILEGE_UNSPECIFIED: _ClassVar[Privilege]
    PRIVILEGE_READ: _ClassVar[Privilege]
    PRIVILEGE_WRITE: _ClassVar[Privilege]
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

class AccessMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACCESS_MODE_UNSPECIFIED: _ClassVar[AccessMode]
    ACCESS_MODE_READ_ONLY: _ClassVar[AccessMode]
    ACCESS_MODE_READ_WRITE: _ClassVar[AccessMode]
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
USER_OPTION_UNSPECIFIED: UserOption
USER_OPTION_SUPERUSER: UserOption
USER_OPTION_NO_SUPERUSER: UserOption
PRIVILEGE_UNSPECIFIED: Privilege
PRIVILEGE_READ: Privilege
PRIVILEGE_WRITE: Privilege
PRIVILEGE_DELETE: Privilege
PRIVILEGE_CREATE: Privilege
PRIVILEGE_DROP: Privilege
PRIVILEGE_TRUNCATE: Privilege
PRIVILEGE_ALTER: Privilege
PRIVILEGE_GRANT: Privilege
POLICY_STATE_UNSPECIFIED: PolicyState
POLICY_STATE_ENABLED: PolicyState
POLICY_STATE_DISABLED: PolicyState
ACCESS_MODE_UNSPECIFIED: AccessMode
ACCESS_MODE_READ_ONLY: AccessMode
ACCESS_MODE_READ_WRITE: AccessMode

class Column(_message.Message):
    __slots__ = ("name", "boolean_value", "int_value", "bigint_value", "float_value", "double_value", "text_value", "blob_value", "date_value", "time_value", "timestamp_value", "timestamptz_value")
    class BooleanValue(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: bool
        def __init__(self, value: bool = ...) -> None: ...
    class IntValue(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: int
        def __init__(self, value: _Optional[int] = ...) -> None: ...
    class BigIntValue(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: int
        def __init__(self, value: _Optional[int] = ...) -> None: ...
    class FloatValue(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: float
        def __init__(self, value: _Optional[float] = ...) -> None: ...
    class DoubleValue(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: float
        def __init__(self, value: _Optional[float] = ...) -> None: ...
    class TextValue(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: str
        def __init__(self, value: _Optional[str] = ...) -> None: ...
    class BlobValue(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: bytes
        def __init__(self, value: _Optional[bytes] = ...) -> None: ...
    class DateValue(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: int
        def __init__(self, value: _Optional[int] = ...) -> None: ...
    class TimeValue(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: int
        def __init__(self, value: _Optional[int] = ...) -> None: ...
    class TimestampValue(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: int
        def __init__(self, value: _Optional[int] = ...) -> None: ...
    class TimestampTZValue(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: int
        def __init__(self, value: _Optional[int] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
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
    name: str
    boolean_value: Column.BooleanValue
    int_value: Column.IntValue
    bigint_value: Column.BigIntValue
    float_value: Column.FloatValue
    double_value: Column.DoubleValue
    text_value: Column.TextValue
    blob_value: Column.BlobValue
    date_value: Column.DateValue
    time_value: Column.TimeValue
    timestamp_value: Column.TimestampValue
    timestamptz_value: Column.TimestampTZValue
    def __init__(self, name: _Optional[str] = ..., boolean_value: _Optional[_Union[Column.BooleanValue, _Mapping]] = ..., int_value: _Optional[_Union[Column.IntValue, _Mapping]] = ..., bigint_value: _Optional[_Union[Column.BigIntValue, _Mapping]] = ..., float_value: _Optional[_Union[Column.FloatValue, _Mapping]] = ..., double_value: _Optional[_Union[Column.DoubleValue, _Mapping]] = ..., text_value: _Optional[_Union[Column.TextValue, _Mapping]] = ..., blob_value: _Optional[_Union[Column.BlobValue, _Mapping]] = ..., date_value: _Optional[_Union[Column.DateValue, _Mapping]] = ..., time_value: _Optional[_Union[Column.TimeValue, _Mapping]] = ..., timestamp_value: _Optional[_Union[Column.TimestampValue, _Mapping]] = ..., timestamptz_value: _Optional[_Union[Column.TimestampTZValue, _Mapping]] = ...) -> None: ...

class Key(_message.Message):
    __slots__ = ("columns",)
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    columns: _containers.RepeatedCompositeFieldContainer[Column]
    def __init__(self, columns: _Optional[_Iterable[_Union[Column, _Mapping]]] = ...) -> None: ...

class Get(_message.Message):
    __slots__ = ("namespace_name", "table_name", "get_type", "partition_key", "clustering_key", "projections", "conjunctions", "attributes")
    class GetType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        GET_TYPE_UNSPECIFIED: _ClassVar[Get.GetType]
        GET_TYPE_GET: _ClassVar[Get.GetType]
        GET_TYPE_GET_WITH_INDEX: _ClassVar[Get.GetType]
    GET_TYPE_UNSPECIFIED: Get.GetType
    GET_TYPE_GET: Get.GetType
    GET_TYPE_GET_WITH_INDEX: Get.GetType
    class Conjunction(_message.Message):
        __slots__ = ("conditional_expressions",)
        CONDITIONAL_EXPRESSIONS_FIELD_NUMBER: _ClassVar[int]
        conditional_expressions: _containers.RepeatedCompositeFieldContainer[ConditionalExpression]
        def __init__(self, conditional_expressions: _Optional[_Iterable[_Union[ConditionalExpression, _Mapping]]] = ...) -> None: ...
    class AttributesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAMESPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    GET_TYPE_FIELD_NUMBER: _ClassVar[int]
    PARTITION_KEY_FIELD_NUMBER: _ClassVar[int]
    CLUSTERING_KEY_FIELD_NUMBER: _ClassVar[int]
    PROJECTIONS_FIELD_NUMBER: _ClassVar[int]
    CONJUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    namespace_name: str
    table_name: str
    get_type: Get.GetType
    partition_key: Key
    clustering_key: Key
    projections: _containers.RepeatedScalarFieldContainer[str]
    conjunctions: _containers.RepeatedCompositeFieldContainer[Get.Conjunction]
    attributes: _containers.ScalarMap[str, str]
    def __init__(self, namespace_name: _Optional[str] = ..., table_name: _Optional[str] = ..., get_type: _Optional[_Union[Get.GetType, str]] = ..., partition_key: _Optional[_Union[Key, _Mapping]] = ..., clustering_key: _Optional[_Union[Key, _Mapping]] = ..., projections: _Optional[_Iterable[str]] = ..., conjunctions: _Optional[_Iterable[_Union[Get.Conjunction, _Mapping]]] = ..., attributes: _Optional[_Mapping[str, str]] = ...) -> None: ...

class Scan(_message.Message):
    __slots__ = ("namespace_name", "table_name", "scan_type", "partition_key", "projections", "start_clustering_key", "start_inclusive", "end_clustering_key", "end_inclusive", "orderings", "limit", "conjunctions", "attributes")
    class ScanType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SCAN_TYPE_UNSPECIFIED: _ClassVar[Scan.ScanType]
        SCAN_TYPE_SCAN: _ClassVar[Scan.ScanType]
        SCAN_TYPE_SCAN_WITH_INDEX: _ClassVar[Scan.ScanType]
        SCAN_TYPE_SCAN_ALL: _ClassVar[Scan.ScanType]
    SCAN_TYPE_UNSPECIFIED: Scan.ScanType
    SCAN_TYPE_SCAN: Scan.ScanType
    SCAN_TYPE_SCAN_WITH_INDEX: Scan.ScanType
    SCAN_TYPE_SCAN_ALL: Scan.ScanType
    class Ordering(_message.Message):
        __slots__ = ("column_name", "order")
        class Order(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ORDER_UNSPECIFIED: _ClassVar[Scan.Ordering.Order]
            ORDER_ASC: _ClassVar[Scan.Ordering.Order]
            ORDER_DESC: _ClassVar[Scan.Ordering.Order]
        ORDER_UNSPECIFIED: Scan.Ordering.Order
        ORDER_ASC: Scan.Ordering.Order
        ORDER_DESC: Scan.Ordering.Order
        COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
        ORDER_FIELD_NUMBER: _ClassVar[int]
        column_name: str
        order: Scan.Ordering.Order
        def __init__(self, column_name: _Optional[str] = ..., order: _Optional[_Union[Scan.Ordering.Order, str]] = ...) -> None: ...
    class Conjunction(_message.Message):
        __slots__ = ("conditional_expressions",)
        CONDITIONAL_EXPRESSIONS_FIELD_NUMBER: _ClassVar[int]
        conditional_expressions: _containers.RepeatedCompositeFieldContainer[ConditionalExpression]
        def __init__(self, conditional_expressions: _Optional[_Iterable[_Union[ConditionalExpression, _Mapping]]] = ...) -> None: ...
    class AttributesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAMESPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    SCAN_TYPE_FIELD_NUMBER: _ClassVar[int]
    PARTITION_KEY_FIELD_NUMBER: _ClassVar[int]
    PROJECTIONS_FIELD_NUMBER: _ClassVar[int]
    START_CLUSTERING_KEY_FIELD_NUMBER: _ClassVar[int]
    START_INCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    END_CLUSTERING_KEY_FIELD_NUMBER: _ClassVar[int]
    END_INCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    ORDERINGS_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    CONJUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    namespace_name: str
    table_name: str
    scan_type: Scan.ScanType
    partition_key: Key
    projections: _containers.RepeatedScalarFieldContainer[str]
    start_clustering_key: Key
    start_inclusive: bool
    end_clustering_key: Key
    end_inclusive: bool
    orderings: _containers.RepeatedCompositeFieldContainer[Scan.Ordering]
    limit: int
    conjunctions: _containers.RepeatedCompositeFieldContainer[Scan.Conjunction]
    attributes: _containers.ScalarMap[str, str]
    def __init__(self, namespace_name: _Optional[str] = ..., table_name: _Optional[str] = ..., scan_type: _Optional[_Union[Scan.ScanType, str]] = ..., partition_key: _Optional[_Union[Key, _Mapping]] = ..., projections: _Optional[_Iterable[str]] = ..., start_clustering_key: _Optional[_Union[Key, _Mapping]] = ..., start_inclusive: bool = ..., end_clustering_key: _Optional[_Union[Key, _Mapping]] = ..., end_inclusive: bool = ..., orderings: _Optional[_Iterable[_Union[Scan.Ordering, _Mapping]]] = ..., limit: _Optional[int] = ..., conjunctions: _Optional[_Iterable[_Union[Scan.Conjunction, _Mapping]]] = ..., attributes: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ConditionalExpression(_message.Message):
    __slots__ = ("column", "operator", "escape")
    class Operator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OPERATOR_UNSPECIFIED: _ClassVar[ConditionalExpression.Operator]
        OPERATOR_EQ: _ClassVar[ConditionalExpression.Operator]
        OPERATOR_NE: _ClassVar[ConditionalExpression.Operator]
        OPERATOR_GT: _ClassVar[ConditionalExpression.Operator]
        OPERATOR_GTE: _ClassVar[ConditionalExpression.Operator]
        OPERATOR_LT: _ClassVar[ConditionalExpression.Operator]
        OPERATOR_LTE: _ClassVar[ConditionalExpression.Operator]
        OPERATOR_IS_NULL: _ClassVar[ConditionalExpression.Operator]
        OPERATOR_IS_NOT_NULL: _ClassVar[ConditionalExpression.Operator]
        OPERATOR_LIKE: _ClassVar[ConditionalExpression.Operator]
        OPERATOR_NOT_LIKE: _ClassVar[ConditionalExpression.Operator]
    OPERATOR_UNSPECIFIED: ConditionalExpression.Operator
    OPERATOR_EQ: ConditionalExpression.Operator
    OPERATOR_NE: ConditionalExpression.Operator
    OPERATOR_GT: ConditionalExpression.Operator
    OPERATOR_GTE: ConditionalExpression.Operator
    OPERATOR_LT: ConditionalExpression.Operator
    OPERATOR_LTE: ConditionalExpression.Operator
    OPERATOR_IS_NULL: ConditionalExpression.Operator
    OPERATOR_IS_NOT_NULL: ConditionalExpression.Operator
    OPERATOR_LIKE: ConditionalExpression.Operator
    OPERATOR_NOT_LIKE: ConditionalExpression.Operator
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    ESCAPE_FIELD_NUMBER: _ClassVar[int]
    column: Column
    operator: ConditionalExpression.Operator
    escape: str
    def __init__(self, column: _Optional[_Union[Column, _Mapping]] = ..., operator: _Optional[_Union[ConditionalExpression.Operator, str]] = ..., escape: _Optional[str] = ...) -> None: ...

class Put(_message.Message):
    __slots__ = ("namespace_name", "table_name", "partition_key", "clustering_key", "columns", "put_condition", "implicit_pre_read_enabled", "insert_mode_enabled", "attributes")
    class PutCondition(_message.Message):
        __slots__ = ("put_condition_type", "conditional_expressions")
        class PutConditionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            PUT_CONDITION_TYPE_UNSPECIFIED: _ClassVar[Put.PutCondition.PutConditionType]
            PUT_CONDITION_TYPE_IF: _ClassVar[Put.PutCondition.PutConditionType]
            PUT_CONDITION_TYPE_IF_EXISTS: _ClassVar[Put.PutCondition.PutConditionType]
            PUT_CONDITION_TYPE_IF_NOT_EXISTS: _ClassVar[Put.PutCondition.PutConditionType]
        PUT_CONDITION_TYPE_UNSPECIFIED: Put.PutCondition.PutConditionType
        PUT_CONDITION_TYPE_IF: Put.PutCondition.PutConditionType
        PUT_CONDITION_TYPE_IF_EXISTS: Put.PutCondition.PutConditionType
        PUT_CONDITION_TYPE_IF_NOT_EXISTS: Put.PutCondition.PutConditionType
        PUT_CONDITION_TYPE_FIELD_NUMBER: _ClassVar[int]
        CONDITIONAL_EXPRESSIONS_FIELD_NUMBER: _ClassVar[int]
        put_condition_type: Put.PutCondition.PutConditionType
        conditional_expressions: _containers.RepeatedCompositeFieldContainer[ConditionalExpression]
        def __init__(self, put_condition_type: _Optional[_Union[Put.PutCondition.PutConditionType, str]] = ..., conditional_expressions: _Optional[_Iterable[_Union[ConditionalExpression, _Mapping]]] = ...) -> None: ...
    class AttributesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAMESPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    PARTITION_KEY_FIELD_NUMBER: _ClassVar[int]
    CLUSTERING_KEY_FIELD_NUMBER: _ClassVar[int]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    PUT_CONDITION_FIELD_NUMBER: _ClassVar[int]
    IMPLICIT_PRE_READ_ENABLED_FIELD_NUMBER: _ClassVar[int]
    INSERT_MODE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    namespace_name: str
    table_name: str
    partition_key: Key
    clustering_key: Key
    columns: _containers.RepeatedCompositeFieldContainer[Column]
    put_condition: Put.PutCondition
    implicit_pre_read_enabled: bool
    insert_mode_enabled: bool
    attributes: _containers.ScalarMap[str, str]
    def __init__(self, namespace_name: _Optional[str] = ..., table_name: _Optional[str] = ..., partition_key: _Optional[_Union[Key, _Mapping]] = ..., clustering_key: _Optional[_Union[Key, _Mapping]] = ..., columns: _Optional[_Iterable[_Union[Column, _Mapping]]] = ..., put_condition: _Optional[_Union[Put.PutCondition, _Mapping]] = ..., implicit_pre_read_enabled: bool = ..., insert_mode_enabled: bool = ..., attributes: _Optional[_Mapping[str, str]] = ...) -> None: ...

class Insert(_message.Message):
    __slots__ = ("namespace_name", "table_name", "partition_key", "clustering_key", "columns", "attributes")
    class AttributesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAMESPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    PARTITION_KEY_FIELD_NUMBER: _ClassVar[int]
    CLUSTERING_KEY_FIELD_NUMBER: _ClassVar[int]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    namespace_name: str
    table_name: str
    partition_key: Key
    clustering_key: Key
    columns: _containers.RepeatedCompositeFieldContainer[Column]
    attributes: _containers.ScalarMap[str, str]
    def __init__(self, namespace_name: _Optional[str] = ..., table_name: _Optional[str] = ..., partition_key: _Optional[_Union[Key, _Mapping]] = ..., clustering_key: _Optional[_Union[Key, _Mapping]] = ..., columns: _Optional[_Iterable[_Union[Column, _Mapping]]] = ..., attributes: _Optional[_Mapping[str, str]] = ...) -> None: ...

class Upsert(_message.Message):
    __slots__ = ("namespace_name", "table_name", "partition_key", "clustering_key", "columns", "attributes")
    class AttributesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAMESPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    PARTITION_KEY_FIELD_NUMBER: _ClassVar[int]
    CLUSTERING_KEY_FIELD_NUMBER: _ClassVar[int]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    namespace_name: str
    table_name: str
    partition_key: Key
    clustering_key: Key
    columns: _containers.RepeatedCompositeFieldContainer[Column]
    attributes: _containers.ScalarMap[str, str]
    def __init__(self, namespace_name: _Optional[str] = ..., table_name: _Optional[str] = ..., partition_key: _Optional[_Union[Key, _Mapping]] = ..., clustering_key: _Optional[_Union[Key, _Mapping]] = ..., columns: _Optional[_Iterable[_Union[Column, _Mapping]]] = ..., attributes: _Optional[_Mapping[str, str]] = ...) -> None: ...

class Update(_message.Message):
    __slots__ = ("namespace_name", "table_name", "partition_key", "clustering_key", "columns", "update_condition", "attributes")
    class UpdateCondition(_message.Message):
        __slots__ = ("update_condition_type", "conditional_expressions")
        class UpdateConditionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UPDATE_CONDITION_TYPE_UNSPECIFIED: _ClassVar[Update.UpdateCondition.UpdateConditionType]
            UPDATE_CONDITION_TYPE_IF: _ClassVar[Update.UpdateCondition.UpdateConditionType]
            UPDATE_CONDITION_TYPE_IF_EXISTS: _ClassVar[Update.UpdateCondition.UpdateConditionType]
        UPDATE_CONDITION_TYPE_UNSPECIFIED: Update.UpdateCondition.UpdateConditionType
        UPDATE_CONDITION_TYPE_IF: Update.UpdateCondition.UpdateConditionType
        UPDATE_CONDITION_TYPE_IF_EXISTS: Update.UpdateCondition.UpdateConditionType
        UPDATE_CONDITION_TYPE_FIELD_NUMBER: _ClassVar[int]
        CONDITIONAL_EXPRESSIONS_FIELD_NUMBER: _ClassVar[int]
        update_condition_type: Update.UpdateCondition.UpdateConditionType
        conditional_expressions: _containers.RepeatedCompositeFieldContainer[ConditionalExpression]
        def __init__(self, update_condition_type: _Optional[_Union[Update.UpdateCondition.UpdateConditionType, str]] = ..., conditional_expressions: _Optional[_Iterable[_Union[ConditionalExpression, _Mapping]]] = ...) -> None: ...
    class AttributesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAMESPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    PARTITION_KEY_FIELD_NUMBER: _ClassVar[int]
    CLUSTERING_KEY_FIELD_NUMBER: _ClassVar[int]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_CONDITION_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    namespace_name: str
    table_name: str
    partition_key: Key
    clustering_key: Key
    columns: _containers.RepeatedCompositeFieldContainer[Column]
    update_condition: Update.UpdateCondition
    attributes: _containers.ScalarMap[str, str]
    def __init__(self, namespace_name: _Optional[str] = ..., table_name: _Optional[str] = ..., partition_key: _Optional[_Union[Key, _Mapping]] = ..., clustering_key: _Optional[_Union[Key, _Mapping]] = ..., columns: _Optional[_Iterable[_Union[Column, _Mapping]]] = ..., update_condition: _Optional[_Union[Update.UpdateCondition, _Mapping]] = ..., attributes: _Optional[_Mapping[str, str]] = ...) -> None: ...

class Delete(_message.Message):
    __slots__ = ("namespace_name", "table_name", "partition_key", "clustering_key", "delete_condition", "attributes")
    class DeleteCondition(_message.Message):
        __slots__ = ("delete_condition_type", "conditional_expressions")
        class DeleteConditionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            DELETE_CONDITION_TYPE_UNSPECIFIED: _ClassVar[Delete.DeleteCondition.DeleteConditionType]
            DELETE_CONDITION_TYPE_IF: _ClassVar[Delete.DeleteCondition.DeleteConditionType]
            DELETE_CONDITION_TYPE_IF_EXISTS: _ClassVar[Delete.DeleteCondition.DeleteConditionType]
        DELETE_CONDITION_TYPE_UNSPECIFIED: Delete.DeleteCondition.DeleteConditionType
        DELETE_CONDITION_TYPE_IF: Delete.DeleteCondition.DeleteConditionType
        DELETE_CONDITION_TYPE_IF_EXISTS: Delete.DeleteCondition.DeleteConditionType
        DELETE_CONDITION_TYPE_FIELD_NUMBER: _ClassVar[int]
        CONDITIONAL_EXPRESSIONS_FIELD_NUMBER: _ClassVar[int]
        delete_condition_type: Delete.DeleteCondition.DeleteConditionType
        conditional_expressions: _containers.RepeatedCompositeFieldContainer[ConditionalExpression]
        def __init__(self, delete_condition_type: _Optional[_Union[Delete.DeleteCondition.DeleteConditionType, str]] = ..., conditional_expressions: _Optional[_Iterable[_Union[ConditionalExpression, _Mapping]]] = ...) -> None: ...
    class AttributesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAMESPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    PARTITION_KEY_FIELD_NUMBER: _ClassVar[int]
    CLUSTERING_KEY_FIELD_NUMBER: _ClassVar[int]
    DELETE_CONDITION_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    namespace_name: str
    table_name: str
    partition_key: Key
    clustering_key: Key
    delete_condition: Delete.DeleteCondition
    attributes: _containers.ScalarMap[str, str]
    def __init__(self, namespace_name: _Optional[str] = ..., table_name: _Optional[str] = ..., partition_key: _Optional[_Union[Key, _Mapping]] = ..., clustering_key: _Optional[_Union[Key, _Mapping]] = ..., delete_condition: _Optional[_Union[Delete.DeleteCondition, _Mapping]] = ..., attributes: _Optional[_Mapping[str, str]] = ...) -> None: ...

class Mutation(_message.Message):
    __slots__ = ("put", "delete", "insert", "upsert", "update")
    PUT_FIELD_NUMBER: _ClassVar[int]
    DELETE_FIELD_NUMBER: _ClassVar[int]
    INSERT_FIELD_NUMBER: _ClassVar[int]
    UPSERT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    put: Put
    delete: Delete
    insert: Insert
    upsert: Upsert
    update: Update
    def __init__(self, put: _Optional[_Union[Put, _Mapping]] = ..., delete: _Optional[_Union[Delete, _Mapping]] = ..., insert: _Optional[_Union[Insert, _Mapping]] = ..., upsert: _Optional[_Union[Upsert, _Mapping]] = ..., update: _Optional[_Union[Update, _Mapping]] = ...) -> None: ...

class Result(_message.Message):
    __slots__ = ("columns",)
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    columns: _containers.RepeatedCompositeFieldContainer[Column]
    def __init__(self, columns: _Optional[_Iterable[_Union[Column, _Mapping]]] = ...) -> None: ...

class TableMetadata(_message.Message):
    __slots__ = ("columns", "partition_key_column_names", "clustering_key_column_names", "clustering_orders", "secondary_index_column_names", "encrypted_columns")
    class ColumnsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: DataType
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[DataType, str]] = ...) -> None: ...
    class ClusteringOrdersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ClusteringOrder
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ClusteringOrder, str]] = ...) -> None: ...
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    PARTITION_KEY_COLUMN_NAMES_FIELD_NUMBER: _ClassVar[int]
    CLUSTERING_KEY_COLUMN_NAMES_FIELD_NUMBER: _ClassVar[int]
    CLUSTERING_ORDERS_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_INDEX_COLUMN_NAMES_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    columns: _containers.ScalarMap[str, DataType]
    partition_key_column_names: _containers.RepeatedScalarFieldContainer[str]
    clustering_key_column_names: _containers.RepeatedScalarFieldContainer[str]
    clustering_orders: _containers.ScalarMap[str, ClusteringOrder]
    secondary_index_column_names: _containers.RepeatedScalarFieldContainer[str]
    encrypted_columns: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, columns: _Optional[_Mapping[str, DataType]] = ..., partition_key_column_names: _Optional[_Iterable[str]] = ..., clustering_key_column_names: _Optional[_Iterable[str]] = ..., clustering_orders: _Optional[_Mapping[str, ClusteringOrder]] = ..., secondary_index_column_names: _Optional[_Iterable[str]] = ..., encrypted_columns: _Optional[_Iterable[str]] = ...) -> None: ...

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

class GetRequest(_message.Message):
    __slots__ = ("request_header", "transaction_id", "get")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    GET_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    transaction_id: str
    get: Get
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., transaction_id: _Optional[str] = ..., get: _Optional[_Union[Get, _Mapping]] = ...) -> None: ...

class GetResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: Result
    def __init__(self, result: _Optional[_Union[Result, _Mapping]] = ...) -> None: ...

class ScanRequest(_message.Message):
    __slots__ = ("request_header", "transaction_id", "scan")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    SCAN_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    transaction_id: str
    scan: Scan
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., transaction_id: _Optional[str] = ..., scan: _Optional[_Union[Scan, _Mapping]] = ...) -> None: ...

class ScanResponse(_message.Message):
    __slots__ = ("results",)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[Result]
    def __init__(self, results: _Optional[_Iterable[_Union[Result, _Mapping]]] = ...) -> None: ...

class PutRequest(_message.Message):
    __slots__ = ("request_header", "transaction_id", "puts")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    PUTS_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    transaction_id: str
    puts: _containers.RepeatedCompositeFieldContainer[Put]
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., transaction_id: _Optional[str] = ..., puts: _Optional[_Iterable[_Union[Put, _Mapping]]] = ...) -> None: ...

class PutResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class InsertRequest(_message.Message):
    __slots__ = ("request_header", "transaction_id", "inserts")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    INSERTS_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    transaction_id: str
    inserts: _containers.RepeatedCompositeFieldContainer[Insert]
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., transaction_id: _Optional[str] = ..., inserts: _Optional[_Iterable[_Union[Insert, _Mapping]]] = ...) -> None: ...

class InsertResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpsertRequest(_message.Message):
    __slots__ = ("request_header", "transaction_id", "upserts")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    UPSERTS_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    transaction_id: str
    upserts: _containers.RepeatedCompositeFieldContainer[Upsert]
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., transaction_id: _Optional[str] = ..., upserts: _Optional[_Iterable[_Union[Upsert, _Mapping]]] = ...) -> None: ...

class UpsertResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateRequest(_message.Message):
    __slots__ = ("request_header", "transaction_id", "updates")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATES_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    transaction_id: str
    updates: _containers.RepeatedCompositeFieldContainer[Update]
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., transaction_id: _Optional[str] = ..., updates: _Optional[_Iterable[_Union[Update, _Mapping]]] = ...) -> None: ...

class UpdateResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteRequest(_message.Message):
    __slots__ = ("request_header", "transaction_id", "deletes")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    DELETES_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    transaction_id: str
    deletes: _containers.RepeatedCompositeFieldContainer[Delete]
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., transaction_id: _Optional[str] = ..., deletes: _Optional[_Iterable[_Union[Delete, _Mapping]]] = ...) -> None: ...

class DeleteResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MutateRequest(_message.Message):
    __slots__ = ("request_header", "transaction_id", "mutations")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    MUTATIONS_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    transaction_id: str
    mutations: _containers.RepeatedCompositeFieldContainer[Mutation]
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., transaction_id: _Optional[str] = ..., mutations: _Optional[_Iterable[_Union[Mutation, _Mapping]]] = ...) -> None: ...

class MutateResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

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

class CreateNamespaceRequest(_message.Message):
    __slots__ = ("namespace_name", "options", "if_not_exists", "request_header")
    class OptionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAMESPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    IF_NOT_EXISTS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    namespace_name: str
    options: _containers.ScalarMap[str, str]
    if_not_exists: bool
    request_header: RequestHeader
    def __init__(self, namespace_name: _Optional[str] = ..., options: _Optional[_Mapping[str, str]] = ..., if_not_exists: bool = ..., request_header: _Optional[_Union[RequestHeader, _Mapping]] = ...) -> None: ...

class CreateNamespaceResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DropNamespaceRequest(_message.Message):
    __slots__ = ("namespace_name", "if_exists", "request_header")
    NAMESPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    namespace_name: str
    if_exists: bool
    request_header: RequestHeader
    def __init__(self, namespace_name: _Optional[str] = ..., if_exists: bool = ..., request_header: _Optional[_Union[RequestHeader, _Mapping]] = ...) -> None: ...

class DropNamespaceResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class NamespaceExistsRequest(_message.Message):
    __slots__ = ("namespace_name", "request_header")
    NAMESPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    namespace_name: str
    request_header: RequestHeader
    def __init__(self, namespace_name: _Optional[str] = ..., request_header: _Optional[_Union[RequestHeader, _Mapping]] = ...) -> None: ...

class NamespaceExistsResponse(_message.Message):
    __slots__ = ("exists",)
    EXISTS_FIELD_NUMBER: _ClassVar[int]
    exists: bool
    def __init__(self, exists: bool = ...) -> None: ...

class CreateTableRequest(_message.Message):
    __slots__ = ("namespace_name", "table_name", "table_metadata", "options", "if_not_exists", "request_header")
    class OptionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAMESPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    TABLE_METADATA_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    IF_NOT_EXISTS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    namespace_name: str
    table_name: str
    table_metadata: TableMetadata
    options: _containers.ScalarMap[str, str]
    if_not_exists: bool
    request_header: RequestHeader
    def __init__(self, namespace_name: _Optional[str] = ..., table_name: _Optional[str] = ..., table_metadata: _Optional[_Union[TableMetadata, _Mapping]] = ..., options: _Optional[_Mapping[str, str]] = ..., if_not_exists: bool = ..., request_header: _Optional[_Union[RequestHeader, _Mapping]] = ...) -> None: ...

class CreateTableResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DropTableRequest(_message.Message):
    __slots__ = ("namespace_name", "table_name", "if_exists", "request_header")
    NAMESPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    namespace_name: str
    table_name: str
    if_exists: bool
    request_header: RequestHeader
    def __init__(self, namespace_name: _Optional[str] = ..., table_name: _Optional[str] = ..., if_exists: bool = ..., request_header: _Optional[_Union[RequestHeader, _Mapping]] = ...) -> None: ...

class DropTableResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TruncateTableRequest(_message.Message):
    __slots__ = ("namespace_name", "table_name", "request_header")
    NAMESPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    namespace_name: str
    table_name: str
    request_header: RequestHeader
    def __init__(self, namespace_name: _Optional[str] = ..., table_name: _Optional[str] = ..., request_header: _Optional[_Union[RequestHeader, _Mapping]] = ...) -> None: ...

class TruncateTableResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TableExistsRequest(_message.Message):
    __slots__ = ("namespace_name", "table_name", "request_header")
    NAMESPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    namespace_name: str
    table_name: str
    request_header: RequestHeader
    def __init__(self, namespace_name: _Optional[str] = ..., table_name: _Optional[str] = ..., request_header: _Optional[_Union[RequestHeader, _Mapping]] = ...) -> None: ...

class TableExistsResponse(_message.Message):
    __slots__ = ("exists",)
    EXISTS_FIELD_NUMBER: _ClassVar[int]
    exists: bool
    def __init__(self, exists: bool = ...) -> None: ...

class CreateIndexRequest(_message.Message):
    __slots__ = ("namespace_name", "table_name", "column_name", "options", "if_not_exists", "request_header")
    class OptionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAMESPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    IF_NOT_EXISTS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    namespace_name: str
    table_name: str
    column_name: str
    options: _containers.ScalarMap[str, str]
    if_not_exists: bool
    request_header: RequestHeader
    def __init__(self, namespace_name: _Optional[str] = ..., table_name: _Optional[str] = ..., column_name: _Optional[str] = ..., options: _Optional[_Mapping[str, str]] = ..., if_not_exists: bool = ..., request_header: _Optional[_Union[RequestHeader, _Mapping]] = ...) -> None: ...

class CreateIndexResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DropIndexRequest(_message.Message):
    __slots__ = ("namespace_name", "table_name", "column_name", "if_exists", "request_header")
    NAMESPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
    IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    namespace_name: str
    table_name: str
    column_name: str
    if_exists: bool
    request_header: RequestHeader
    def __init__(self, namespace_name: _Optional[str] = ..., table_name: _Optional[str] = ..., column_name: _Optional[str] = ..., if_exists: bool = ..., request_header: _Optional[_Union[RequestHeader, _Mapping]] = ...) -> None: ...

class DropIndexResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class IndexExistsRequest(_message.Message):
    __slots__ = ("namespace_name", "table_name", "column_name", "request_header")
    NAMESPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    namespace_name: str
    table_name: str
    column_name: str
    request_header: RequestHeader
    def __init__(self, namespace_name: _Optional[str] = ..., table_name: _Optional[str] = ..., column_name: _Optional[str] = ..., request_header: _Optional[_Union[RequestHeader, _Mapping]] = ...) -> None: ...

class IndexExistsResponse(_message.Message):
    __slots__ = ("exists",)
    EXISTS_FIELD_NUMBER: _ClassVar[int]
    exists: bool
    def __init__(self, exists: bool = ...) -> None: ...

class RepairTableRequest(_message.Message):
    __slots__ = ("namespace_name", "table_name", "table_metadata", "options", "request_header")
    class OptionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAMESPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    TABLE_METADATA_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    namespace_name: str
    table_name: str
    table_metadata: TableMetadata
    options: _containers.ScalarMap[str, str]
    request_header: RequestHeader
    def __init__(self, namespace_name: _Optional[str] = ..., table_name: _Optional[str] = ..., table_metadata: _Optional[_Union[TableMetadata, _Mapping]] = ..., options: _Optional[_Mapping[str, str]] = ..., request_header: _Optional[_Union[RequestHeader, _Mapping]] = ...) -> None: ...

class RepairTableResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AddNewColumnToTableRequest(_message.Message):
    __slots__ = ("namespace_name", "table_name", "column_name", "column_data_type", "request_header", "encrypted")
    NAMESPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
    COLUMN_DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_FIELD_NUMBER: _ClassVar[int]
    namespace_name: str
    table_name: str
    column_name: str
    column_data_type: DataType
    request_header: RequestHeader
    encrypted: bool
    def __init__(self, namespace_name: _Optional[str] = ..., table_name: _Optional[str] = ..., column_name: _Optional[str] = ..., column_data_type: _Optional[_Union[DataType, str]] = ..., request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., encrypted: bool = ...) -> None: ...

class AddNewColumnToTableResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateCoordinatorTablesRequest(_message.Message):
    __slots__ = ("options", "if_not_exist", "request_header")
    class OptionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    IF_NOT_EXIST_FIELD_NUMBER: _ClassVar[int]
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    options: _containers.ScalarMap[str, str]
    if_not_exist: bool
    request_header: RequestHeader
    def __init__(self, options: _Optional[_Mapping[str, str]] = ..., if_not_exist: bool = ..., request_header: _Optional[_Union[RequestHeader, _Mapping]] = ...) -> None: ...

class CreateCoordinatorTablesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DropCoordinatorTablesRequest(_message.Message):
    __slots__ = ("if_exist", "request_header")
    IF_EXIST_FIELD_NUMBER: _ClassVar[int]
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    if_exist: bool
    request_header: RequestHeader
    def __init__(self, if_exist: bool = ..., request_header: _Optional[_Union[RequestHeader, _Mapping]] = ...) -> None: ...

class DropCoordinatorTablesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TruncateCoordinatorTablesRequest(_message.Message):
    __slots__ = ("request_header",)
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ...) -> None: ...

class TruncateCoordinatorTablesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CoordinatorTablesExistRequest(_message.Message):
    __slots__ = ("request_header",)
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ...) -> None: ...

class CoordinatorTablesExistResponse(_message.Message):
    __slots__ = ("exist",)
    EXIST_FIELD_NUMBER: _ClassVar[int]
    exist: bool
    def __init__(self, exist: bool = ...) -> None: ...

class RepairCoordinatorTablesRequest(_message.Message):
    __slots__ = ("options", "request_header")
    class OptionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    options: _containers.ScalarMap[str, str]
    request_header: RequestHeader
    def __init__(self, options: _Optional[_Mapping[str, str]] = ..., request_header: _Optional[_Union[RequestHeader, _Mapping]] = ...) -> None: ...

class RepairCoordinatorTablesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetTableMetadataRequest(_message.Message):
    __slots__ = ("namespace_name", "table_name", "request_header")
    NAMESPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    namespace_name: str
    table_name: str
    request_header: RequestHeader
    def __init__(self, namespace_name: _Optional[str] = ..., table_name: _Optional[str] = ..., request_header: _Optional[_Union[RequestHeader, _Mapping]] = ...) -> None: ...

class GetTableMetadataResponse(_message.Message):
    __slots__ = ("table_metadata",)
    TABLE_METADATA_FIELD_NUMBER: _ClassVar[int]
    table_metadata: TableMetadata
    def __init__(self, table_metadata: _Optional[_Union[TableMetadata, _Mapping]] = ...) -> None: ...

class GetNamespaceNamesRequest(_message.Message):
    __slots__ = ("request_header",)
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ...) -> None: ...

class GetNamespaceNamesResponse(_message.Message):
    __slots__ = ("namespace_names",)
    NAMESPACE_NAMES_FIELD_NUMBER: _ClassVar[int]
    namespace_names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, namespace_names: _Optional[_Iterable[str]] = ...) -> None: ...

class GetNamespaceTableNamesRequest(_message.Message):
    __slots__ = ("namespace_name", "request_header")
    NAMESPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    namespace_name: str
    request_header: RequestHeader
    def __init__(self, namespace_name: _Optional[str] = ..., request_header: _Optional[_Union[RequestHeader, _Mapping]] = ...) -> None: ...

class GetNamespaceTableNamesResponse(_message.Message):
    __slots__ = ("table_names",)
    TABLE_NAMES_FIELD_NUMBER: _ClassVar[int]
    table_names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, table_names: _Optional[_Iterable[str]] = ...) -> None: ...

class ImportTableRequest(_message.Message):
    __slots__ = ("namespace_name", "table_name", "options", "request_header", "override_columns_type")
    class OptionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class OverrideColumnsTypeEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: DataType
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[DataType, str]] = ...) -> None: ...
    NAMESPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_COLUMNS_TYPE_FIELD_NUMBER: _ClassVar[int]
    namespace_name: str
    table_name: str
    options: _containers.ScalarMap[str, str]
    request_header: RequestHeader
    override_columns_type: _containers.ScalarMap[str, DataType]
    def __init__(self, namespace_name: _Optional[str] = ..., table_name: _Optional[str] = ..., options: _Optional[_Mapping[str, str]] = ..., request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., override_columns_type: _Optional[_Mapping[str, DataType]] = ...) -> None: ...

class ImportTableResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateUserRequest(_message.Message):
    __slots__ = ("request_header", "username", "password", "user_options")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    USER_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    username: str
    password: str
    user_options: _containers.RepeatedScalarFieldContainer[UserOption]
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., username: _Optional[str] = ..., password: _Optional[str] = ..., user_options: _Optional[_Iterable[_Union[UserOption, str]]] = ...) -> None: ...

class CreateUserResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AlterUserRequest(_message.Message):
    __slots__ = ("request_header", "username", "password", "user_options")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    USER_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    username: str
    password: str
    user_options: _containers.RepeatedScalarFieldContainer[UserOption]
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., username: _Optional[str] = ..., password: _Optional[str] = ..., user_options: _Optional[_Iterable[_Union[UserOption, str]]] = ...) -> None: ...

class AlterUserResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DropUserRequest(_message.Message):
    __slots__ = ("request_header", "username")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    username: str
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., username: _Optional[str] = ...) -> None: ...

class DropUserResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GrantRequest(_message.Message):
    __slots__ = ("request_header", "username", "namespace_name", "table_name", "privileges")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    PRIVILEGES_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    username: str
    namespace_name: str
    table_name: str
    privileges: _containers.RepeatedScalarFieldContainer[Privilege]
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., username: _Optional[str] = ..., namespace_name: _Optional[str] = ..., table_name: _Optional[str] = ..., privileges: _Optional[_Iterable[_Union[Privilege, str]]] = ...) -> None: ...

class GrantResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RevokeRequest(_message.Message):
    __slots__ = ("request_header", "username", "namespace_name", "table_name", "privileges")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    PRIVILEGES_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    username: str
    namespace_name: str
    table_name: str
    privileges: _containers.RepeatedScalarFieldContainer[Privilege]
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., username: _Optional[str] = ..., namespace_name: _Optional[str] = ..., table_name: _Optional[str] = ..., privileges: _Optional[_Iterable[_Union[Privilege, str]]] = ...) -> None: ...

class RevokeResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class User(_message.Message):
    __slots__ = ("name", "superuser")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SUPERUSER_FIELD_NUMBER: _ClassVar[int]
    name: str
    superuser: bool
    def __init__(self, name: _Optional[str] = ..., superuser: bool = ...) -> None: ...

class GetUserRequest(_message.Message):
    __slots__ = ("request_header", "username")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    username: str
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., username: _Optional[str] = ...) -> None: ...

class GetUserResponse(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: User
    def __init__(self, user: _Optional[_Union[User, _Mapping]] = ...) -> None: ...

class GetUsersRequest(_message.Message):
    __slots__ = ("request_header",)
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ...) -> None: ...

class GetUsersResponse(_message.Message):
    __slots__ = ("users",)
    USERS_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[User]
    def __init__(self, users: _Optional[_Iterable[_Union[User, _Mapping]]] = ...) -> None: ...

class GetCurrentUserRequest(_message.Message):
    __slots__ = ("request_header",)
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ...) -> None: ...

class GetCurrentUserResponse(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: User
    def __init__(self, user: _Optional[_Union[User, _Mapping]] = ...) -> None: ...

class GetPrivilegesRequest(_message.Message):
    __slots__ = ("request_header", "username", "namespace_name", "table_name")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    username: str
    namespace_name: str
    table_name: str
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., username: _Optional[str] = ..., namespace_name: _Optional[str] = ..., table_name: _Optional[str] = ...) -> None: ...

class GetPrivilegesResponse(_message.Message):
    __slots__ = ("privileges",)
    PRIVILEGES_FIELD_NUMBER: _ClassVar[int]
    privileges: _containers.RepeatedScalarFieldContainer[Privilege]
    def __init__(self, privileges: _Optional[_Iterable[_Union[Privilege, str]]] = ...) -> None: ...

class CreatePolicyRequest(_message.Message):
    __slots__ = ("request_header", "policy_name", "data_tag_column_name")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_TAG_COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    policy_name: str
    data_tag_column_name: str
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., policy_name: _Optional[str] = ..., data_tag_column_name: _Optional[str] = ...) -> None: ...

class CreatePolicyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EnablePolicyRequest(_message.Message):
    __slots__ = ("request_header", "policy_name")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    policy_name: str
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., policy_name: _Optional[str] = ...) -> None: ...

class EnablePolicyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DisablePolicyRequest(_message.Message):
    __slots__ = ("request_header", "policy_name")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    policy_name: str
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., policy_name: _Optional[str] = ...) -> None: ...

class DisablePolicyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetPolicyRequest(_message.Message):
    __slots__ = ("request_header", "policy_name")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    policy_name: str
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., policy_name: _Optional[str] = ...) -> None: ...

class GetPolicyResponse(_message.Message):
    __slots__ = ("policy",)
    POLICY_FIELD_NUMBER: _ClassVar[int]
    policy: Policy
    def __init__(self, policy: _Optional[_Union[Policy, _Mapping]] = ...) -> None: ...

class GetPoliciesRequest(_message.Message):
    __slots__ = ("request_header",)
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ...) -> None: ...

class GetPoliciesResponse(_message.Message):
    __slots__ = ("policies",)
    POLICIES_FIELD_NUMBER: _ClassVar[int]
    policies: _containers.RepeatedCompositeFieldContainer[Policy]
    def __init__(self, policies: _Optional[_Iterable[_Union[Policy, _Mapping]]] = ...) -> None: ...

class CreateLevelRequest(_message.Message):
    __slots__ = ("request_header", "policy_name", "level_short_name", "level_long_name", "level_number")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    LEVEL_SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
    LEVEL_LONG_NAME_FIELD_NUMBER: _ClassVar[int]
    LEVEL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    policy_name: str
    level_short_name: str
    level_long_name: str
    level_number: int
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., policy_name: _Optional[str] = ..., level_short_name: _Optional[str] = ..., level_long_name: _Optional[str] = ..., level_number: _Optional[int] = ...) -> None: ...

class CreateLevelResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DropLevelRequest(_message.Message):
    __slots__ = ("request_header", "policy_name", "level_short_name")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    LEVEL_SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    policy_name: str
    level_short_name: str
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., policy_name: _Optional[str] = ..., level_short_name: _Optional[str] = ...) -> None: ...

class DropLevelResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetLevelRequest(_message.Message):
    __slots__ = ("request_header", "policy_name", "level_short_name")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    LEVEL_SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    policy_name: str
    level_short_name: str
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., policy_name: _Optional[str] = ..., level_short_name: _Optional[str] = ...) -> None: ...

class GetLevelResponse(_message.Message):
    __slots__ = ("level",)
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    level: Level
    def __init__(self, level: _Optional[_Union[Level, _Mapping]] = ...) -> None: ...

class GetLevelsRequest(_message.Message):
    __slots__ = ("request_header", "policy_name")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    policy_name: str
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., policy_name: _Optional[str] = ...) -> None: ...

class GetLevelsResponse(_message.Message):
    __slots__ = ("levels",)
    LEVELS_FIELD_NUMBER: _ClassVar[int]
    levels: _containers.RepeatedCompositeFieldContainer[Level]
    def __init__(self, levels: _Optional[_Iterable[_Union[Level, _Mapping]]] = ...) -> None: ...

class CreateCompartmentRequest(_message.Message):
    __slots__ = ("request_header", "policy_name", "compartment_short_name", "compartment_long_name")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    COMPARTMENT_SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
    COMPARTMENT_LONG_NAME_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    policy_name: str
    compartment_short_name: str
    compartment_long_name: str
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., policy_name: _Optional[str] = ..., compartment_short_name: _Optional[str] = ..., compartment_long_name: _Optional[str] = ...) -> None: ...

class CreateCompartmentResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DropCompartmentRequest(_message.Message):
    __slots__ = ("request_header", "policy_name", "compartment_short_name")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    COMPARTMENT_SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    policy_name: str
    compartment_short_name: str
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., policy_name: _Optional[str] = ..., compartment_short_name: _Optional[str] = ...) -> None: ...

class DropCompartmentResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetCompartmentRequest(_message.Message):
    __slots__ = ("request_header", "policy_name", "compartment_short_name")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    COMPARTMENT_SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    policy_name: str
    compartment_short_name: str
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., policy_name: _Optional[str] = ..., compartment_short_name: _Optional[str] = ...) -> None: ...

class GetCompartmentResponse(_message.Message):
    __slots__ = ("compartment",)
    COMPARTMENT_FIELD_NUMBER: _ClassVar[int]
    compartment: Compartment
    def __init__(self, compartment: _Optional[_Union[Compartment, _Mapping]] = ...) -> None: ...

class GetCompartmentsRequest(_message.Message):
    __slots__ = ("request_header", "policy_name")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    policy_name: str
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., policy_name: _Optional[str] = ...) -> None: ...

class GetCompartmentsResponse(_message.Message):
    __slots__ = ("compartments",)
    COMPARTMENTS_FIELD_NUMBER: _ClassVar[int]
    compartments: _containers.RepeatedCompositeFieldContainer[Compartment]
    def __init__(self, compartments: _Optional[_Iterable[_Union[Compartment, _Mapping]]] = ...) -> None: ...

class CreateGroupRequest(_message.Message):
    __slots__ = ("request_header", "policy_name", "group_short_name", "group_long_name", "parent_group_short_name")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    GROUP_SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
    GROUP_LONG_NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_GROUP_SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    policy_name: str
    group_short_name: str
    group_long_name: str
    parent_group_short_name: str
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., policy_name: _Optional[str] = ..., group_short_name: _Optional[str] = ..., group_long_name: _Optional[str] = ..., parent_group_short_name: _Optional[str] = ...) -> None: ...

class CreateGroupResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DropGroupRequest(_message.Message):
    __slots__ = ("request_header", "policy_name", "group_short_name")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    GROUP_SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    policy_name: str
    group_short_name: str
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., policy_name: _Optional[str] = ..., group_short_name: _Optional[str] = ...) -> None: ...

class DropGroupResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetGroupRequest(_message.Message):
    __slots__ = ("request_header", "policy_name", "group_short_name")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    GROUP_SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    policy_name: str
    group_short_name: str
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., policy_name: _Optional[str] = ..., group_short_name: _Optional[str] = ...) -> None: ...

class GetGroupResponse(_message.Message):
    __slots__ = ("group",)
    GROUP_FIELD_NUMBER: _ClassVar[int]
    group: Group
    def __init__(self, group: _Optional[_Union[Group, _Mapping]] = ...) -> None: ...

class GetGroupsRequest(_message.Message):
    __slots__ = ("request_header", "policy_name")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    policy_name: str
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., policy_name: _Optional[str] = ...) -> None: ...

class GetGroupsResponse(_message.Message):
    __slots__ = ("groups",)
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    groups: _containers.RepeatedCompositeFieldContainer[Group]
    def __init__(self, groups: _Optional[_Iterable[_Union[Group, _Mapping]]] = ...) -> None: ...

class SetLevelsToUserRequest(_message.Message):
    __slots__ = ("request_header", "policy_name", "username", "level_short_name", "default_level_short_name", "row_level_short_name")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    LEVEL_SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_LEVEL_SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
    ROW_LEVEL_SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    policy_name: str
    username: str
    level_short_name: str
    default_level_short_name: str
    row_level_short_name: str
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., policy_name: _Optional[str] = ..., username: _Optional[str] = ..., level_short_name: _Optional[str] = ..., default_level_short_name: _Optional[str] = ..., row_level_short_name: _Optional[str] = ...) -> None: ...

class SetLevelsToUserResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AddCompartmentToUserRequest(_message.Message):
    __slots__ = ("request_header", "policy_name", "username", "compartment_short_name", "access_mode", "default_compartment", "row_compartment")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    COMPARTMENT_SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
    ACCESS_MODE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_COMPARTMENT_FIELD_NUMBER: _ClassVar[int]
    ROW_COMPARTMENT_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    policy_name: str
    username: str
    compartment_short_name: str
    access_mode: AccessMode
    default_compartment: bool
    row_compartment: bool
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., policy_name: _Optional[str] = ..., username: _Optional[str] = ..., compartment_short_name: _Optional[str] = ..., access_mode: _Optional[_Union[AccessMode, str]] = ..., default_compartment: bool = ..., row_compartment: bool = ...) -> None: ...

class AddCompartmentToUserResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RemoveCompartmentFromUserRequest(_message.Message):
    __slots__ = ("request_header", "policy_name", "username", "compartment_short_name")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    COMPARTMENT_SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    policy_name: str
    username: str
    compartment_short_name: str
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., policy_name: _Optional[str] = ..., username: _Optional[str] = ..., compartment_short_name: _Optional[str] = ...) -> None: ...

class RemoveCompartmentFromUserResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AddGroupToUserRequest(_message.Message):
    __slots__ = ("request_header", "policy_name", "username", "group_short_name", "access_mode", "default_group", "row_group")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    GROUP_SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
    ACCESS_MODE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_GROUP_FIELD_NUMBER: _ClassVar[int]
    ROW_GROUP_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    policy_name: str
    username: str
    group_short_name: str
    access_mode: AccessMode
    default_group: bool
    row_group: bool
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., policy_name: _Optional[str] = ..., username: _Optional[str] = ..., group_short_name: _Optional[str] = ..., access_mode: _Optional[_Union[AccessMode, str]] = ..., default_group: bool = ..., row_group: bool = ...) -> None: ...

class AddGroupToUserResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RemoveGroupFromUserRequest(_message.Message):
    __slots__ = ("request_header", "policy_name", "username", "group_short_name")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    GROUP_SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    policy_name: str
    username: str
    group_short_name: str
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., policy_name: _Optional[str] = ..., username: _Optional[str] = ..., group_short_name: _Optional[str] = ...) -> None: ...

class RemoveGroupFromUserResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DropUserTagInfoFromUserRequest(_message.Message):
    __slots__ = ("request_header", "policy_name", "username")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    policy_name: str
    username: str
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., policy_name: _Optional[str] = ..., username: _Optional[str] = ...) -> None: ...

class DropUserTagInfoFromUserResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

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

class CreateNamespacePolicyRequest(_message.Message):
    __slots__ = ("request_header", "namespace_policy_name", "policy_name", "namespace_name")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    namespace_policy_name: str
    policy_name: str
    namespace_name: str
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., namespace_policy_name: _Optional[str] = ..., policy_name: _Optional[str] = ..., namespace_name: _Optional[str] = ...) -> None: ...

class CreateNamespacePolicyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EnableNamespacePolicyRequest(_message.Message):
    __slots__ = ("request_header", "namespace_policy_name")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    namespace_policy_name: str
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., namespace_policy_name: _Optional[str] = ...) -> None: ...

class EnableNamespacePolicyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DisableNamespacePolicyRequest(_message.Message):
    __slots__ = ("request_header", "namespace_policy_name")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    namespace_policy_name: str
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., namespace_policy_name: _Optional[str] = ...) -> None: ...

class DisableNamespacePolicyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetNamespacePolicyRequest(_message.Message):
    __slots__ = ("request_header", "namespace_policy_name")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    namespace_policy_name: str
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., namespace_policy_name: _Optional[str] = ...) -> None: ...

class GetNamespacePolicyResponse(_message.Message):
    __slots__ = ("namespace_policy",)
    NAMESPACE_POLICY_FIELD_NUMBER: _ClassVar[int]
    namespace_policy: NamespacePolicy
    def __init__(self, namespace_policy: _Optional[_Union[NamespacePolicy, _Mapping]] = ...) -> None: ...

class GetNamespacePoliciesRequest(_message.Message):
    __slots__ = ("request_header",)
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ...) -> None: ...

class GetNamespacePoliciesResponse(_message.Message):
    __slots__ = ("namespace_policies",)
    NAMESPACE_POLICIES_FIELD_NUMBER: _ClassVar[int]
    namespace_policies: _containers.RepeatedCompositeFieldContainer[NamespacePolicy]
    def __init__(self, namespace_policies: _Optional[_Iterable[_Union[NamespacePolicy, _Mapping]]] = ...) -> None: ...

class CreateTablePolicyRequest(_message.Message):
    __slots__ = ("request_header", "table_policy_name", "policy_name", "namespace_name", "table_name")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    TABLE_POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    table_policy_name: str
    policy_name: str
    namespace_name: str
    table_name: str
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., table_policy_name: _Optional[str] = ..., policy_name: _Optional[str] = ..., namespace_name: _Optional[str] = ..., table_name: _Optional[str] = ...) -> None: ...

class CreateTablePolicyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EnableTablePolicyRequest(_message.Message):
    __slots__ = ("request_header", "table_policy_name")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    TABLE_POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    table_policy_name: str
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., table_policy_name: _Optional[str] = ...) -> None: ...

class EnableTablePolicyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DisableTablePolicyRequest(_message.Message):
    __slots__ = ("request_header", "table_policy_name")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    TABLE_POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    table_policy_name: str
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., table_policy_name: _Optional[str] = ...) -> None: ...

class DisableTablePolicyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetTablePolicyRequest(_message.Message):
    __slots__ = ("request_header", "table_policy_name")
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    TABLE_POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    table_policy_name: str
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ..., table_policy_name: _Optional[str] = ...) -> None: ...

class GetTablePolicyResponse(_message.Message):
    __slots__ = ("table_policy",)
    TABLE_POLICY_FIELD_NUMBER: _ClassVar[int]
    table_policy: TablePolicy
    def __init__(self, table_policy: _Optional[_Union[TablePolicy, _Mapping]] = ...) -> None: ...

class GetTablePoliciesRequest(_message.Message):
    __slots__ = ("request_header",)
    REQUEST_HEADER_FIELD_NUMBER: _ClassVar[int]
    request_header: RequestHeader
    def __init__(self, request_header: _Optional[_Union[RequestHeader, _Mapping]] = ...) -> None: ...

class GetTablePoliciesResponse(_message.Message):
    __slots__ = ("table_policies",)
    TABLE_POLICIES_FIELD_NUMBER: _ClassVar[int]
    table_policies: _containers.RepeatedCompositeFieldContainer[TablePolicy]
    def __init__(self, table_policies: _Optional[_Iterable[_Union[TablePolicy, _Mapping]]] = ...) -> None: ...

class Policy(_message.Message):
    __slots__ = ("name", "data_tag_column_name", "state")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_TAG_COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    data_tag_column_name: str
    state: PolicyState
    def __init__(self, name: _Optional[str] = ..., data_tag_column_name: _Optional[str] = ..., state: _Optional[_Union[PolicyState, str]] = ...) -> None: ...

class Level(_message.Message):
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

class Compartment(_message.Message):
    __slots__ = ("policy_name", "short_name", "long_name")
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
    LONG_NAME_FIELD_NUMBER: _ClassVar[int]
    policy_name: str
    short_name: str
    long_name: str
    def __init__(self, policy_name: _Optional[str] = ..., short_name: _Optional[str] = ..., long_name: _Optional[str] = ...) -> None: ...

class Group(_message.Message):
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

class NamespacePolicy(_message.Message):
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

class TablePolicy(_message.Message):
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
