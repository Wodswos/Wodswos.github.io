https://docs.github.com/en/actions

读官方文档，顺便摘录一下，不然总感觉啥也没干没学进去——虽然 copy 一下也依旧没学进去。

# 概述

Github Actions  是 Github 于 2018年 10 月推出的持续集成服务。Jenkins 就是常用的持续集成平台工具。

![](C:/Users/Five/Desktop/note/img/overview-actions-simple.png)

![](C:/Users/Five/Desktop/note/img/overview-actions-event.png)

- `workflow（工作流程）`：持续集成一次运行的过程，就是一个`workflow`。
  - on：触发 workflow 的条件，常用的有 push （即 git 提交操作，可以任意指定分支），pull_request，release，workflow_dispatch （手动触发）等，详见 https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows
  - permission：
  - concurrency：
- `job（任务）`：一个`workflow`由一个或多个`jobs`构成，含义是一次持续集成的运行，可以完成多个任务。
  - 每个 job 运行在自己的虚拟机 runner 或者容器中，即意味着一个Job中的若干个Steps可以共享数据
    - runs-on 配置运行环境，Github 提供 Ubuntu，Windows，Mac OS 等 runner，也可以使用自己的服务器。
  - 默认情况下 job 之间没有依赖且并行执行，可以通过 needs 配置 job 间的依赖
- `step（步骤）` & `action（动作）`：每个 jobs 由多个 `step` 组成，每个 step 可以执行 action 或者其他命令。
  - Action 是Github Acitons 平台自定义的应用，是可复用的拓展，用于简化 workflow

限制：每个 workflow 运行时限 72 小时，每小时最多执行 1000 个 API 请求。当然，这种限制对大部分正常的小项目而言，Github Action 可以说是基本没有限制的慈善行为了。

> 一个repo可以有多个Workflow
>
> 可以在一个Workflow中引用另一个Workflow

在现有的 workflow （actions marketplace）里搜索 pages 有若干结果

* Astro
* Gatsby
* Hugo
* Github Pages Jekyll
* Jekyll
* Next.js
* Static HTML
* Fortify on Demand Scan



## Jobs 概述

![](C:/Users/Five/Desktop/note/img/overview-actions-event.png)

### Demo: 构建 Jekyll Site 的 job

最简单的 Jekyll site 构建和部署包含 build 和 deploy 两个 job，以及相应的若干属性

```yaml
jobs:
  # Build job
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3
      - name: Setup Pages
        uses: actions/configure-pages@v2
      - name: Build with Jekyll
        uses: actions/jekyll-build-pages@v1
        with:
          source: ./
          destination: ./_site
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v1

  # Deployment job
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v1
```

### 其他 job 常用字段

strategy: 可以配置 strategy.matrix 变量，用于对不同环境（or 版本） or 不同语言（or 版本） or 不同工具的情景分别执行 job

* A matrix strategy lets you use variables in a single job definition to automatically create multiple job runs that are based on the combinations of the variables. 
* 即会穷举 strategy.matrix 中的每种环境配置组合各自进行独立的 job （如 3 * 3 * 2 的矩阵则会执行18个Job）

```yaml
jobs:
  example_matrix:
    strategy:
      matrix:
        version: [10, 12, 14]
    steps:
      - uses: actions/setup-node@v3
        with:
          node-version: ${{ matrix.version }}
```

## Steps & Action 概述

The actions you use in your workflow can be defined in:

- The same repository as your workflow file
- Any public repository
- A published Docker container image on Docker Hub

### uses & run





### 常用 Actions 和 Marketplace







### write your own actions

https://docs.github.com/en/actions/creating-actions





## starter workflows



![image-20221209162955851](C:\Users\Five\Desktop\note\img\image-20221209162955851.png)



# Learn Github Actions

https://docs.github.com/en/actions/learn-github-actions/

## Understand Github Actions

https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions

GitHub Actions is a continuous integration and continuous delivery (CI/CD) platform that allows you to automate your build, test, and deployment pipeline.

![](C:/Users/Five/Desktop/note/img/overview-actions-simple.png)





## Find and customize actions







# Examples





# Using workflows





# Using jobs





# Manage workflow runs



# Build and test





# Deployment



# Containerized Services





# Publish package





# Manage issues and pull requests



# Migrate to Github Actions



# Monitor & troubleshoot



# Github-hosted runners



# Self-hosted runners



# Security guides



# Creating Actions



## Abount custom actions

You can build Docker container, JavaScript, and composite actions.

Actions require a metadate file to define the inputs, outputs and main entrypoint for your action. The metadata must filename must be either `action.yml` or `action.yaml`.



### action.yaml

如下所示是 checkout@v3 的 `action.yml`

```yaml
name: 'Checkout'
description: 'Checkout a Git repository at a particular version'
inputs:
  repository:
    description: 'Repository name with owner. For example, actions/checkout'
    default: ${{ github.repository }}
  ref:
    description: >
      The branch, tag or SHA to checkout. When checking out the repository that
      triggered a workflow, this defaults to the reference or SHA for that
      event.  Otherwise, uses the default branch.
  token:
    description: >
      Personal access token (PAT) used to fetch the repository. The PAT is configured
      with the local git config, which enables your scripts to run authenticated git
      commands. The post-job step removes the PAT.


      We recommend using a service account with the least permissions necessary.
      Also when generating a new PAT, select the least scopes necessary.


      [Learn more about creating and using encrypted secrets](https://help.github.com/en/actions/automating-your-workflow-with-github-actions/creating-and-using-encrypted-secrets)
    default: ${{ github.token }}
  ssh-key:
    description: >
      SSH key used to fetch the repository. The SSH key is configured with the local
      git config, which enables your scripts to run authenticated git commands.
      The post-job step removes the SSH key.


      We recommend using a service account with the least permissions necessary.


      [Learn more about creating and using
      encrypted secrets](https://help.github.com/en/actions/automating-your-workflow-with-github-actions/creating-and-using-encrypted-secrets)
  ssh-known-hosts:
    description: >
      Known hosts in addition to the user and global host key database. The public
      SSH keys for a host may be obtained using the utility `ssh-keyscan`. For example,
      `ssh-keyscan github.com`. The public key for github.com is always implicitly added.
  ssh-strict:
    description: >
      Whether to perform strict host key checking. When true, adds the options `StrictHostKeyChecking=yes`
      and `CheckHostIP=no` to the SSH command line. Use the input `ssh-known-hosts` to
      configure additional hosts.
    default: true
  persist-credentials:
    description: 'Whether to configure the token or SSH key with the local git config'
    default: true
  path:
    description: 'Relative path under $GITHUB_WORKSPACE to place the repository'
  clean:
    description: 'Whether to execute `git clean -ffdx && git reset --hard HEAD` before fetching'
    default: true
  fetch-depth:
    description: 'Number of commits to fetch. 0 indicates all history for all branches and tags.'
    default: 1
  lfs:
    description: 'Whether to download Git-LFS files'
    default: false
  submodules:
    description: >
      Whether to checkout submodules: `true` to checkout submodules or `recursive` to
      recursively checkout submodules.


      When the `ssh-key` input is not provided, SSH URLs beginning with `git@github.com:` are
      converted to HTTPS.
    default: false
  set-safe-directory:
    description: Add repository path as safe.directory for Git global config by running `git config --global --add safe.directory <path>`
    default: true
  github-server-url:
    description: The base URL for the GitHub instance that you are trying to clone from, will use environment defaults to fetch from the same instance that the workflow is running from unless specified. Example URLs are https://github.com or https://my-ghes-server.example.com
    required: false
runs:
  using: node16
  main: dist/index.js
  post: dist/index.js

```



# Guides for Github Actions





