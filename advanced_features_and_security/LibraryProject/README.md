# LibraryProject
# Django Permissions and Groups Setup

## Custom Permissions

- Added custom permissions `can_view`, `can_create`, `can_edit`, and `can_delete` to the `Book` model in `relationship_app`.

## Groups and Permissions

- Groups created: `Viewers`, `Editors`, `Admins`.
- Permissions assigned:
  - Viewers: `can_view`
  - Editors: `can_view`, `can_create`, `can_edit`
  - Admins: `can_view`, `can_create`, `can_edit`, `can_delete`

## How to Create Groups

Run the custom management command:


## Enforcing Permissions in Views

- Views are protected using the `@permission_required('relationship_app.can_action', raise_exception=True)` decorator.
- This restricts access based on the logged-in user's permissions.

## Testing

- Assign users to groups via Django admin.
- Attempt to access views and verify access restrictions.
