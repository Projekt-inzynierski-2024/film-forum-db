CREATE DATABASE [UsersDb]
GO

USE [UsersDb]
GO

/****** Object:  Table [dbo].[request_logs]    Script Date: 09.11.2023 21:31:21 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[request_logs](
    [id] [int] IDENTITY(1,1) NOT NULL,
    [user_id] [int] NOT NULL,
    [request_path] [nvarchar](200) NOT NULL,
    [ip_address] [nvarchar](200) NOT NULL,
    [http_method] [nvarchar](200) NOT NULL,
    [status_code] [int] NOT NULL,
    [sent_at] [datetime] NOT NULL
) ON [PRIMARY]
GO


/****** Object:  Table [dbo].[role]    Script Date: 09.11.2023 21:31:09 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[role](
    [id] [int] IDENTITY(1,1) NOT NULL,
    [name] [nvarchar](100) NOT NULL,
 CONSTRAINT [PK_role] PRIMARY KEY CLUSTERED 
(
    [id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO


/****** Object:  Table [dbo].[user_diagnostics]    Script Date: 09.11.2023 21:30:50 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[user_diagnostics](
    [id] [int] IDENTITY(1,1) NOT NULL,
    [user_id] [int] NOT NULL,
    [created_at] [datetime] NOT NULL,
    [last_successfull_sign_in] [datetime] NOT NULL,
    [last_failed_sign_in] [datetime] NULL,
    [last_username_change] [datetime] NULL,
    [last_email_change] [datetime] NULL,
    [last_password_change] [datetime] NULL,
 CONSTRAINT [PK_user_diagnostics] PRIMARY KEY CLUSTERED 
(
    [id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO


/****** Object:  Table [dbo].[users]    Script Date: 09.11.2023 21:30:07 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[users](
    [id] [int] IDENTITY(1,1) NOT NULL,
    [username] [nvarchar](200) NOT NULL,
    [email] [nvarchar](200) NOT NULL,
    [password] [nvarchar](200) NOT NULL,
    [2fa]   [bit] DEFAULT(0) NOT NULL,
    [recover_password_token] [nvarchar](200) NULL,
    [recover_password_token_expiration] [datetime] NULL,
    [created_at] [datetime] NOT NULL,
 CONSTRAINT [PK_users] PRIMARY KEY CLUSTERED 
(
    [id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO


/****** Object:  Table [dbo].[user_to_role]    Script Date: 09.11.2023 21:30:37 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[user_to_role](
    [id] [int] IDENTITY(1,1) NOT NULL,
    [role_id] [int] NOT NULL,
    [user_id] [int] NOT NULL,
 CONSTRAINT [PK_user_to_role] PRIMARY KEY CLUSTERED 
(
    [id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

-- inserts

INSERT INTO role (name) VALUES ('Admin'), ('Moderator'), ('User');
GO
