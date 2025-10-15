erDiagram
    users {
        SERIAL id PK
        VARCHAR username
        VARCHAR email
        VARCHAR password_hash
        VARCHAR first_name
        VARCHAR last_name
        TEXT bio
        VARCHAR avatar_url
        TIMESTAMP created_at
        TIMESTAMP updated_at
        BOOLEAN is_active
    }

    categories {
        SERIAL id PK
        VARCHAR name
        TEXT description
        VARCHAR color
        TIMESTAMP created_at
    }

    posts {
        SERIAL id PK
        VARCHAR title
        TEXT content
        TEXT excerpt
        INTEGER author_id FK
        VARCHAR status
        VARCHAR featured_image_url
        TIMESTAMP created_at
        TIMESTAMP updated_at
        TIMESTAMP published_at
        INTEGER view_count
    }

    post_categories {
        INTEGER post_id FK
        INTEGER category_id FK
        TIMESTAMP created_at
    }

    favorites {
        SERIAL id PK
        INTEGER user_id FK
        INTEGER post_id FK
        TIMESTAMP created_at
    }

    comments {
        SERIAL id PK
        TEXT content
        INTEGER author_id FK
        INTEGER post_id FK
        INTEGER parent_comment_id FK
        TIMESTAMP created_at
        TIMESTAMP updated_at
        BOOLEAN is_edited
    }

    subscriptions {
        SERIAL id PK
        INTEGER subscriber_id FK
        INTEGER target_user_id FK
        TIMESTAMP created_at
    }

    users ||--o{ posts : "author"
    users ||--o{ favorites : "user"
    users ||--o{ comments : "author"
    users ||--o{ subscriptions : "subscriber"
    users ||--o{ subscriptions : "target_user"
    posts ||--o{ favorites : "post"
    posts ||--o{ comments : "post"
    posts }o--|| post_categories : "post"
    categories }o--|| post_categories : "category"
    comments }o--|| comments : "parent_comment"