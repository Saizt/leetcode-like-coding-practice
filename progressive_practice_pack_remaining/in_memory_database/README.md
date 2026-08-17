# In-Memory Database

Implement an in-memory database.

The problem is divided into multiple levels. New functionality is introduced progressively.
All behavior required by earlier levels must continue to work.

---

# Level 1

The database stores records identified by string keys.

Each record contains string fields mapped to integer values.

## Operations

### `set(key: str, field: str, value: int) -> None`

Sets `field` in the record identified by `key` to `value`.

- If the record does not exist, create it.
- If the field already exists, replace its value.

### `get(key: str, field: str) -> int | None`

Returns the value of `field` in the record identified by `key`.

- If the key or field does not exist, return `None`.

### `delete(key: str, field: str) -> bool`

Deletes `field` from the record identified by `key`.

- Return `True` if the field existed and was deleted.
- Return `False` otherwise.
- If deleting the field leaves the record empty, the record may be removed.

---

# Level 2

The database should now support listing fields of a record.

## New Operations

### `scan(key: str) -> list[str]`

Returns all fields belonging to the specified record.

Each field must be formatted as:

`"<field>(<value>)"`

Results must be ordered by field name in ascending lexicographical order.

If the record does not exist, return an empty list.

### `scan_by_prefix(key: str, prefix: str) -> list[str]`

Returns fields belonging to the specified record whose field names start with `prefix`.

Formatting and ordering are the same as for `scan`.

If the record does not exist or no fields match, return an empty list.

---

# Level 3

The database should now support timestamped operations and time-to-live (TTL).

Timestamped operations use integer timestamps. Calls will be supplied in non-decreasing timestamp order.

Fields written through timestamped operations may optionally expire.

## New Operations

### `set_at(key: str, field: str, value: int, timestamp: int) -> None`

Sets a field beginning at `timestamp`.

The value remains valid until replaced, deleted, or expired.

### `set_at_with_ttl(key: str, field: str, value: int, timestamp: int, ttl: int) -> None`

Sets a field beginning at `timestamp`.

The field is valid for timestamps in the half-open interval:

`[timestamp, timestamp + ttl)`

At `timestamp + ttl`, the field is considered expired.

### `get_at(key: str, field: str, timestamp: int) -> int | None`

Returns the value visible at the specified timestamp.

Expired or deleted fields must behave as nonexistent.

### `delete_at(key: str, field: str, timestamp: int) -> bool`

Deletes the field if it exists at the specified timestamp.

Return `True` if a visible field was deleted, otherwise `False`.

### `scan_at(key: str, timestamp: int) -> list[str]`

Equivalent to `scan`, but only fields visible at the specified timestamp are returned.

### `scan_by_prefix_at(key: str, prefix: str, timestamp: int) -> list[str]`

Equivalent to `scan_by_prefix`, but only fields visible at the specified timestamp are returned.

## Requirements

- Expired fields must not appear in reads or scans.
- A later write to the same field replaces the previous value and expiration behavior.
- A write without TTL remains valid until replaced or deleted.
- All functionality from Levels 1 and 2 must continue to work.

---

# Level 4

The database should now support backup and restore.

A backup captures the database state visible at a specific timestamp.

## New Operations

### `backup(timestamp: int) -> int`

Creates a snapshot of all records and fields visible at `timestamp`.

For fields with TTL, the backup must preserve their remaining lifetime rather than the original absolute expiration time.

Return the number of non-empty records stored in the backup.

Multiple backups may be created.

### `restore(timestamp: int, restore_timestamp: int) -> None`

Restores the database using the latest backup created at or before `restore_timestamp`.

If no such backup exists, restore an empty database.

The restored state becomes active at `timestamp`.

For fields that had a remaining TTL at backup time, their expiration must be shifted so that the same remaining lifetime begins from the restore operation's `timestamp`.

Fields without TTL remain non-expiring after restore.

## Requirements

- Restore replaces the current database state.
- Backups are immutable snapshots.
- Restoring must not modify previously stored backups.
- The latest backup whose backup timestamp is less than or equal to `restore_timestamp` must be selected.
- All previous-level behavior must continue to work.
