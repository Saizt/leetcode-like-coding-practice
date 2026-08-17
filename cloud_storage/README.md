Cloud Storage

Implement an in-memory cloud storage system.

The problem is divided into multiple levels.

All behavior required by previous levels must continue to work as new levels are introduced.

⸻

Level 1

The cloud storage system should support adding files, retrieving file sizes, and deleting files.

Operations

add_file(name: str, size: int) -> bool

Adds a new file with the specified name and size.

* If a file with the same name already exists, return False and make no changes.
* Otherwise, add the file and return True.

get_file_size(name: str) -> int | None

Returns the size of the specified file.

* If the file exists, return its size.
* If the file does not exist, return None.

delete_file(name: str) -> int | None

Deletes the specified file.

* If the file exists, remove it and return its size.
* If the file does not exist, return None.

Requirements

* File names are unique.
* File sizes are positive integers.
* All operations should behave exactly as specified.





⸻

Level 2

The cloud storage system should now support searching for files by prefix and suffix.

All functionality from previous levels must continue to work.

New Operation

find_file(prefix: str, suffix: str) -> list[str]

Finds all files whose names:

* start with prefix
* end with suffix

Matching files must be ordered by:

1. File size in descending order.
2. File name in ascending lexicographical order when file sizes are equal.

Each result must be returned in the following format:

"<name>(<size>)"

If no files match the specified prefix and suffix, return an empty list.

Requirements

* All Level 1 functionality must continue to work.
* Both the prefix and suffix conditions must be satisfied for a file to match.
* Search operations must not modify the stored files.





⸻

Level 3 

The cloud storage system should now support users with storage capacity limits.

All functionality from previous levels must continue to work.

Users

Each user has a maximum storage capacity.

Files added by a user consume that user’s available capacity.

Files created through the original add_file operation are considered system-owned and do not consume user capacity.

New Operations

add_user(user_id: str, capacity: int) -> bool

Adds a new user with the specified storage capacity.

* If the user already exists, return False.
* Otherwise, create the user and return True.

add_file_by(user_id: str, name: str, size: int) -> int | None

Attempts to add a file owned by the specified user.

The operation succeeds only if:

* the user exists
* the file name does not already exist
* the user has enough remaining capacity

If successful:

* add the file
* associate the file with the user
* reduce the user’s remaining capacity by the file size
* return the user’s remaining capacity

If the operation fails, return None and make no changes.

merge_users(target_user_id: str, source_user_id: str) -> int | None

Attempts to merge the source user into the target user.

The operation succeeds only if:

* both users exist
* the users are different

If successful:

* all files owned by the source user become owned by the target user
* the source user’s remaining capacity is added to the target user’s remaining capacity
* the source user is removed
* return the target user’s remaining capacity

If the operation fails, return None.

Deleting Files

When a user-owned file is deleted, its size must be restored to the remaining capacity of the user who owns it.

Deleting a system-owned file does not affect any user capacity.

Requirements

* All Level 1 and Level 2 functionality must continue to work.
* File names remain globally unique.
* User capacity must never become negative.
* Failed operations must not modify storage state.
* File ownership must remain correct after user merges.





⸻

Level 4

The cloud storage system should now support backing up and restoring user files.

All functionality from previous levels must continue to work.

User Backups

A backup stores a snapshot of all files currently owned by a user.

The backup records each file’s name and size at the time the backup is created.

System-owned files are never included in user backups.

New Operations

backup_user(user_id: str) -> int | None

Creates a backup of all files currently owned by the specified user.

* If the user does not exist, return None.
* The new backup replaces any previous backup for that user.
* Return the number of files stored in the backup.

Creating a backup must not modify any files, ownership information, or user capacity.

restore_user(user_id: str) -> int | None

Restores the specified user’s files from their most recent backup.

* If the user does not exist, return None.
* Before restoring, remove all files currently owned by that user and return their sizes to the user’s available capacity.
* If the user has a backup, attempt to restore each file contained in that backup.
* A backed-up file may be restored only if no file with the same name currently exists in storage.
* Restored files keep their original names and sizes and remain owned by the restored user.
* Restoring a file consumes the corresponding amount of the user’s capacity.
* Files that cannot be restored because their names are already in use must be skipped.
* Return the number of files successfully restored.

If the user has no backup, restoring the user removes all of their currently owned files and returns 0.

Backup Independence

A backup is a snapshot.

Changes made after a backup is created must not modify the stored backup.

Deleting, adding, or modifying ownership of files after a backup must not affect the contents of an existing backup.

Creating another backup for the same user replaces the previous snapshot.

User Merging

When users are merged:

* Any backup belonging to the source user is removed together with the source user.
* The target user’s existing backup, if any, remains unchanged.
* Files transferred from the source user to the target user are not automatically added to the target user’s backup.

Requirements

* All functionality from Levels 1–3 must continue to work.
* Backups must contain only user-owned files.
* Restoring must correctly update file ownership and available capacity.
* Existing files owned by other users or by the system must not be overwritten.
* A backup must remain unchanged until explicitly replaced by another backup.