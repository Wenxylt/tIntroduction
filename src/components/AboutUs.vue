<template>
  <main>
    <div class="wapper">
    <MainNav />
      <h3>关于我们</h3>
      <article>
        <section>
          <h4>团队介绍</h4>
          <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介绍介</p>
        </section>
        <section>
          <h4>团队成员</h4>
          <div class="menb-card" v-for="(intro,index) in intros" :key="index">
            <div class="menb-intro">
              <img alt="name" :src="image" />
              <!-- 这里是介绍 -->
              <div class="intro-cont">
                <div>
                  <p>姓名：</p>
                  <p>{{intro.name}}</p>
                </div>
                <div v-for="(item,index) in intro.attr" :key="index">
                  <p>{{item.attr+'：'}}</p>
                  <p>{{item.cont}}</p>
                </div>
              </div>
            </div>
          </div>
        </section>
      </article>
    </div>
  </main>
</template>

<script>
import axios from 'axios'
import MainNav from '@/components/MainNav.vue'
import image from '@/assets/name.jpg'

export default {
  name: 'AboutUs',
  components: {
    MainNav
  },
  data() {
    return {
      crumb: ['首页', '关于我们'],
      intros: [
        {
          id: 0,
          name: '陈晓璐',
          attr: [
            {
              attr: '爱好',
              cont: '宅和花钱'
            },
            {
              attr: '喜欢的食物',
              cont: '串串、紫芋小丸子珍珠奶茶、没有刺的鱼'
            },
            {
              attr: '最近高兴的事情',
              cont: '《集合吧！动物之森》了解一下，匠心巨作猛男必玩！ 我的好友编号：491813612605！欢迎来岛一起养老'
            }
          ]
        }
      ],
      image
    }
  },
  mounted() {
    debugger
    this.getIntros()
  },
  methods: {
    getIntros() {
      debugger
      const service = axios.create({
        baseURL: '', // url = base url + request url
        timeout: 5000 // request timeout
      })
      service({
        url: '/intro',
        method: 'get'
      }).then(response => {
        this.intros = response.data
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
@import '@/styles/variables.scss';
@import '@/styles/mixin.scss';
.wapper {
  position: relative;
  border: 1px solid #bbb;
  border-top: 5px solid $blue;
  background-color: #ffffff;
  box-sizing: border-box;
  @include  wapper;
  h3 {
    padding: 20px 50px;
    font-size: 2rem;
    font-weight: normal;
    height: 100%;
    padding-bottom: 20px;
  }
  article {
    border-top: 1px solid #bbb;
    padding: 20px 50px;
    section {
      padding: 0 10px 20px 0;
      h4 {
        padding-bottom: 10px;
        font-weight: bold;
      }
      .menb-card {
        width: 100%;
        height: 140px;
        margin-bottom: 10px;
        position: relative;
        border: 1px solid #bbb;
        .menb-intro {
          position: absolute;
          left: 45px;
          top: 10px;
          img {
            width: 120px;
            height: 120px;
          }
          .intro-cont {
            position: absolute;
            width: 450px;
            left: 150px;
            top: 5px;
            div {
              width: 100%;
              margin-bottom: 2px;
              flex-direction: row;
              p {
                display: inline-block;
              }
            }
          }
        }
      }
      .decor-box {
        width: 20%;
        height: 100%;
        background-color: $blue;
        position: absolute;
        right: 0;
      }
    }
  }
}
</style>
